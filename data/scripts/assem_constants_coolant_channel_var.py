import openmc
import numpy as np
from numpy import sin, cos, tan, pi
from assem_constants import *

def circle_centers(center_point, radius, stop_before, stop_after):
    circle_centers_before = list(np.arange(center_point-radius, stop_before, -radius*2))
    circle_centers_after = list(np.arange(center_point+radius, stop_after, radius*2))
    return circle_centers_before, circle_centers_after

# remove inward flibe
P_left_x_starting_point = pc.H_side_big - pc.D_to_center_width -  pc.F_len - 2 * pc.F_A1_D_gap +\
           pc.P_small_gap / tan(pi/3) - pc.P_D_jut_hyp + pc.P_A1_adj
P_y_starting_point = P_starting_point - pc.P_A1_height

def remove_inward_flibe(radius_vals, P_cells, D_cell):
    P_left_x, P_y = P_left_x_starting_point, P_y_starting_point
    for j in range(10):
        radius = radius_vals[int(j/2)]
        P_middle_x = P_left_x + pc.P_len/2
        circle_centers_before, circle_centers_after = \
            circle_centers(center_point=P_middle_x, 
                           radius=radius,
                           stop_before=P_left_x+pc.P_D_jut_hyp+radius,
                           stop_after=P_left_x+pc.P_len-pc.P_D_jut_hyp-radius)
        P_bot = openmc.YPlane(y0=P_y)
        anti_spheres = openmc.Cell(fill=flibe)
        for i, origin in enumerate(circle_centers_after):
            if (i % 2) == 0:
                cylinder = openmc.ZCylinder(r=radius, x0=origin, y0=P_y)
                if (j % 2) == 0:
                    P_bot_dir = +P_bot
                else:
                    P_bot_dir = -P_bot
                if anti_spheres.region:
                    anti_spheres.region |= -cylinder & P_bot_dir
                else:
                    anti_spheres.region = -cylinder & P_bot_dir
        for i, origin in enumerate(circle_centers_before):
            if (i % 2) == 1:
                cylinder = openmc.ZCylinder(r=radius, x0=origin, y0=P_y)
                if (j % 2) == 0:
                    P_bot_dir = +P_bot
                else:
                    P_bot_dir = -P_bot
                if anti_spheres.region:
                    anti_spheres.region |= -cylinder & P_bot_dir
                else:
                    anti_spheres.region = -cylinder & P_bot_dir
        P_cells[int(j/2)].region &= ~anti_spheres.region
        D_cell.region |= anti_spheres.region
        if (j %2) == 0:
            P_left_x += pc.P_big_gap / tan(pi/3)
            P_y -= pc.P_big_gap
        else:
            P_left_x += pc.P_A1_adj
            P_y -= pc.P_A1_height
    return P_cells, D_cell

# add outer graphite 
def add_outer_graphite(radius_vals, P_cells, D_cell):
    P_left_x, P_y = P_left_x_starting_point, P_y_starting_point
    for j in range(10):
        radius = radius_vals[int(j/2)]
        P_middle_x = P_left_x + pc.P_len/2
        circle_centers_before, circle_centers_after = \
            circle_centers(center_point=P_middle_x, 
                           radius=radius,
                           stop_before=P_left_x+pc.P_D_jut_hyp+radius,
                           stop_after=P_left_x+pc.P_len-pc.P_D_jut_hyp-radius)
        P_bot = openmc.YPlane(y0=P_y)
        plus_spheres = openmc.Cell(fill=p_graphite)
        for i, origin in enumerate(circle_centers_after):
            if (i % 2) == 1:
                cylinder = openmc.ZCylinder(r=radius, x0=origin, y0=P_y)
                if (j % 2) == 0:
                    P_bot_dir = -P_bot
                else:
                    P_bot_dir = +P_bot
                if plus_spheres.region:
                    plus_spheres.region |= -cylinder & P_bot_dir
                else:
                    plus_spheres.region = -cylinder & P_bot_dir
        for i, origin in enumerate(circle_centers_before):
            if (i % 2) == 0:
                cylinder = openmc.ZCylinder(r=radius, x0=origin, y0=P_y)
                if (j % 2) == 0:
                    P_bot_dir = -P_bot
                else:
                    P_bot_dir = +P_bot
                if plus_spheres.region:
                    plus_spheres.region |= -cylinder & P_bot_dir
                else:
                    plus_spheres.region = -cylinder & P_bot_dir
        P_cells[int(j/2)].region |= plus_spheres.region
        D_cell.region &= ~plus_spheres.region
        if (j %2) == 0:
            P_left_x += pc.P_big_gap / tan(pi/3)
            P_y -= pc.P_big_gap
        else:
            P_left_x += pc.P_A1_adj
            P_y -= pc.P_A1_height
    return P_cells, D_cell
