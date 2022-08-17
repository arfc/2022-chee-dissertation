import numpy as np
from numpy import sin
import openmc
from plank_constants import *

center_point = 2+23.1 - 23.1/2

x_left = openmc.XPlane(x0=0, boundary_type="reflective")
x_right = openmc.XPlane(x0=27.1, boundary_type="reflective")
y_top = openmc.YPlane(y0=3.25, boundary_type="reflective")
y_bot =  openmc.YPlane(y0=0, boundary_type="reflective")
z_top = openmc.ZPlane(z0=T_pitch*20, boundary_type="reflective")
z_bot = openmc.ZPlane(z0=0, boundary_type="reflective")
plank_x_left = openmc.XPlane(x0=2)
plank_x_right = openmc.XPlane(x0=2+23.1)
plank_y_top = openmc.YPlane(y0=2.55)
plank_y_bot = openmc.YPlane(y0=0.35+0.35)
graphite1_x_right = openmc.XPlane(x0=2)
graphite2_x_left = openmc.XPlane(x0=25.1)
flibe_bot_top = openmc.YPlane(y0=0.35)
flibe_top_bot = openmc.YPlane(y0=0.35+2.55)

def circle_centers(center_point, radius):
    circle_centers_before = list(np.arange(center_point-radius, 2+radius, -radius*2))
    circle_centers_after = list(np.arange(center_point+radius, 23.1+2-radius, radius*2))
    return circle_centers_before, circle_centers_after

def remove_inward_flibe(bottom, radius, flibe_region):
    circle_centers_before, circle_centers_after = circle_centers(center_point=center_point, radius=radius)
    anti_spheres = openmc.Cell(fill=flibe)
    if bottom:
        y_axis = 0.35
        flibe_untouched = +y_bot & -flibe_bot_top & +plank_x_left & -plank_x_right & -z_top & +z_bot
        val1, val2 = 1, 0
    else: 
        y_axis = 2.90
        flibe_untouched = +flibe_top_bot & -y_top & +plank_x_left & -plank_x_right & -z_top & +z_bot
        val1, val2 = 0, 1
    for i, origin in enumerate(circle_centers_after):
        cylinder = openmc.ZCylinder(r=radius, x0=origin, y0=y_axis)
        if (i % 2) == val1:
            if anti_spheres.region:
                anti_spheres.region |= (flibe_untouched & -cylinder & -plank_x_right)
            else:
                anti_spheres.region = (flibe_untouched & -cylinder)
    for i, origin in enumerate(circle_centers_before):
        cylinder = openmc.ZCylinder(r=radius, x0=origin, y0=y_axis)
        if (i % 2) == val2:
            if anti_spheres.region: 
                anti_spheres.region |= (flibe_untouched & -cylinder & +plank_x_left)
            else:
                anti_spheres.region = (flibe_untouched & -cylinder)
    flibe_region &= ~anti_spheres.region
    return flibe_region

def add_outward_flibe(bottom, radius, flibe_region):
    circle_centers_before, circle_centers_after = circle_centers(center_point=center_point, radius=radius)
    if bottom:
        y_axis = 0.35
        val1, val2 = 0, 1
    else: 
        y_axis = 2.90
        val1, val2 = 1, 0
    for i, origin in enumerate(circle_centers_after):
        cylinder = openmc.ZCylinder(r=radius, x0=origin, y0=y_axis)
        if (i % 2) == val1:
            flibe_region |= (-cylinder & -plank_x_right)
    for i, origin in enumerate(circle_centers_before):
        cylinder = openmc.ZCylinder(r=radius, x0=origin, y0=y_axis)
        if (i % 2) == val2:
            flibe_region |= (-cylinder & +plank_x_left)
    return flibe_region

def add_graphite_fillers(flibe_bot_region, flibe_top_region):
    graphite_filler_bot = openmc.Cell(fill=lm_graphite, cell_id=30001)
    graphite_filler_top = openmc.Cell(fill=lm_graphite, cell_id=30002)
    flibe_bot_extra = +y_bot &- openmc.YPlane(y0=0.70) & +plank_x_left & -plank_x_right & -z_top & +z_bot
    flibe_top_extra = +openmc.YPlane(y0=2.55) & -y_top & +plank_x_left & -plank_x_right & -z_top & +z_bot
    graphite_filler_bot.region = flibe_bot_extra & ~flibe_bot_region 
    graphite_filler_top.region = flibe_top_extra & ~flibe_top_region
    return graphite_filler_bot, graphite_filler_top

def add_fuel_cells(total_pf, sine_a, sine_b, sine_c, constant):
    boundaries = np.arange(2,27.1,2.31) 
    vol_total = 23.1 * 1.85 * T_pitch * 20
    vol_slice = 2.31 * 1.85 * T_pitch * 20
    vol_triso = 4 / 3 * pi * T_r5 ** 3
    no_trisos = total_pf * vol_total / vol_triso
    midpoints = [] 
    for x in range(len(boundaries)-1):
        midpoints.append((boundaries[x]+boundaries[x+1])/2)
    midpoints = np.array(midpoints)
    sine_val = sine_a * sin(sine_b * midpoints + sine_c) + 2
    sine_val = np.where(sine_val<0, 0, sine_val)
    triso_z = sine_val / sum(sine_val) * no_trisos
    pf_z = triso_z * vol_triso / vol_slice
    if constant:
        pf_z = [total_pf] * 10 
    fuel_cells = {}
    for i in range(len(boundaries)-1):
        fuel_region = (+openmc.XPlane(x0=boundaries[i]) 
               & -openmc.XPlane(x0=boundaries[i+1]) 
               & -plank_y_top & +plank_y_bot 
               & -z_top & +z_bot)
        fuel_cells[i] = create_lattice(fuel_region, pf_z[i], 'prism_cell_'+str(i+1), 40001+i*10000)
    return fuel_cells 