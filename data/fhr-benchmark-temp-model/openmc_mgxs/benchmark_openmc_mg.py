import openmc
import numpy as np
from numpy import sin, cos, tan, pi
import sys
sys.path.insert(1, '../../../../fhr-benchmark-1/scripts/')
from phase1a_constants import *
from tallies import *
sys.path.insert(1, '../../../../moltres/python')
from moltres_xs import *  # noqa: E402

# materials 
outer_flibe = openmc.Material(name='outer_flibe', material_id=0) 
outer_flibe.add_macroscopic('outer_flibe') 
graphite_structure = openmc.Material(name='graphite_structure', material_id=1) 
graphite_structure.add_macroscopic('graphite_structure') 
spacers = openmc.Material(name='spacers', material_id=2) 
spacers.add_macroscopic('spacers') 
slot_flibe = openmc.Material(name='slot_flibe', material_id=3) 
slot_flibe.add_macroscopic('slot_flibe') 
inner_flibe_1 = openmc.Material(name='inner_flibe_1', material_id=4) 
inner_flibe_1.add_macroscopic('inner_flibe_1') 
inner_flibe_2 = openmc.Material(name='inner_flibe_2', material_id=5) 
inner_flibe_2.add_macroscopic('inner_flibe_2') 
inner_flibe_3 = openmc.Material(name='inner_flibe_3', material_id=6) 
inner_flibe_3.add_macroscopic('inner_flibe_3') 
P_1_1 = openmc.Material(name='P_1_1', material_id=7) 
P_1_1.add_macroscopic('P_1_1') 
P_1_2 = openmc.Material(name='P_1_2', material_id=8) 
P_1_2.add_macroscopic('P_1_2') 
P_1_3 = openmc.Material(name='P_1_3', material_id=9) 
P_1_3.add_macroscopic('P_1_3') 
P_1_4 = openmc.Material(name='P_1_4', material_id=10) 
P_1_4.add_macroscopic('P_1_4') 
P_1_5 = openmc.Material(name='P_1_5', material_id=11) 
P_1_5.add_macroscopic('P_1_5') 
P_1_6 = openmc.Material(name='P_1_6', material_id=12) 
P_1_6.add_macroscopic('P_1_6') 
P_2_1 = openmc.Material(name='P_2_1', material_id=13) 
P_2_1.add_macroscopic('P_2_1') 
P_2_2 = openmc.Material(name='P_2_2', material_id=14) 
P_2_2.add_macroscopic('P_2_2') 
P_2_3 = openmc.Material(name='P_2_3', material_id=15) 
P_2_3.add_macroscopic('P_2_3') 
P_2_4 = openmc.Material(name='P_2_4', material_id=16) 
P_2_4.add_macroscopic('P_2_4') 
P_2_5 = openmc.Material(name='P_2_5', material_id=17) 
P_2_5.add_macroscopic('P_2_5') 
P_2_6 = openmc.Material(name='P_2_6', material_id=18) 
P_2_6.add_macroscopic('P_2_6') 
P_3_1 = openmc.Material(name='P_3_1', material_id=19) 
P_3_1.add_macroscopic('P_3_1') 
P_3_2 = openmc.Material(name='P_3_2', material_id=20) 
P_3_2.add_macroscopic('P_3_2') 
P_3_3 = openmc.Material(name='P_3_3', material_id=21) 
P_3_3.add_macroscopic('P_3_3') 
P_3_4 = openmc.Material(name='P_3_4', material_id=22) 
P_3_4.add_macroscopic('P_3_4') 
P_3_5 = openmc.Material(name='P_3_5', material_id=23) 
P_3_5.add_macroscopic('P_3_5') 
P_3_6 = openmc.Material(name='P_3_6', material_id=24) 
P_3_6.add_macroscopic('P_3_6') 
fuel_1_1 = openmc.Material(name='fuel_1_1', material_id=25) 
fuel_1_1.add_macroscopic('fuel_1_1') 
fuel_1_2 = openmc.Material(name='fuel_1_2', material_id=26) 
fuel_1_2.add_macroscopic('fuel_1_2') 
fuel_1_3 = openmc.Material(name='fuel_1_3', material_id=27) 
fuel_1_3.add_macroscopic('fuel_1_3') 
fuel_1_4 = openmc.Material(name='fuel_1_4', material_id=28) 
fuel_1_4.add_macroscopic('fuel_1_4') 
fuel_1_5 = openmc.Material(name='fuel_1_5', material_id=29) 
fuel_1_5.add_macroscopic('fuel_1_5') 
fuel_1_6 = openmc.Material(name='fuel_1_6', material_id=30) 
fuel_1_6.add_macroscopic('fuel_1_6') 
fuel_1_7 = openmc.Material(name='fuel_1_7', material_id=31) 
fuel_1_7.add_macroscopic('fuel_1_7') 
fuel_1_8 = openmc.Material(name='fuel_1_8', material_id=32) 
fuel_1_8.add_macroscopic('fuel_1_8') 
fuel_1_9 = openmc.Material(name='fuel_1_9', material_id=33) 
fuel_1_9.add_macroscopic('fuel_1_9') 
fuel_1_10 = openmc.Material(name='fuel_1_10', material_id=34) 
fuel_1_10.add_macroscopic('fuel_1_10') 
fuel_1_11 = openmc.Material(name='fuel_1_11', material_id=35) 
fuel_1_11.add_macroscopic('fuel_1_11') 
fuel_1_12 = openmc.Material(name='fuel_1_12', material_id=36) 
fuel_1_12.add_macroscopic('fuel_1_12') 
fuel_2_1 = openmc.Material(name='fuel_2_1', material_id=37) 
fuel_2_1.add_macroscopic('fuel_2_1') 
fuel_2_2 = openmc.Material(name='fuel_2_2', material_id=38) 
fuel_2_2.add_macroscopic('fuel_2_2') 
fuel_2_3 = openmc.Material(name='fuel_2_3', material_id=39) 
fuel_2_3.add_macroscopic('fuel_2_3') 
fuel_2_4 = openmc.Material(name='fuel_2_4', material_id=40) 
fuel_2_4.add_macroscopic('fuel_2_4') 
fuel_2_5 = openmc.Material(name='fuel_2_5', material_id=41) 
fuel_2_5.add_macroscopic('fuel_2_5') 
fuel_2_6 = openmc.Material(name='fuel_2_6', material_id=42) 
fuel_2_6.add_macroscopic('fuel_2_6') 
fuel_2_7 = openmc.Material(name='fuel_2_7', material_id=43) 
fuel_2_7.add_macroscopic('fuel_2_7') 
fuel_2_8 = openmc.Material(name='fuel_2_8', material_id=44) 
fuel_2_8.add_macroscopic('fuel_2_8') 
fuel_2_9 = openmc.Material(name='fuel_2_9', material_id=45) 
fuel_2_9.add_macroscopic('fuel_2_9') 
fuel_2_10 = openmc.Material(name='fuel_2_10', material_id=46) 
fuel_2_10.add_macroscopic('fuel_2_10') 
fuel_2_11 = openmc.Material(name='fuel_2_11', material_id=47) 
fuel_2_11.add_macroscopic('fuel_2_11') 
fuel_2_12 = openmc.Material(name='fuel_2_12', material_id=48) 
fuel_2_12.add_macroscopic('fuel_2_12') 
fuel_3_1 = openmc.Material(name='fuel_3_1', material_id=49) 
fuel_3_1.add_macroscopic('fuel_3_1') 
fuel_3_2 = openmc.Material(name='fuel_3_2', material_id=50) 
fuel_3_2.add_macroscopic('fuel_3_2') 
fuel_3_3 = openmc.Material(name='fuel_3_3', material_id=51) 
fuel_3_3.add_macroscopic('fuel_3_3') 
fuel_3_4 = openmc.Material(name='fuel_3_4', material_id=52) 
fuel_3_4.add_macroscopic('fuel_3_4') 
fuel_3_5 = openmc.Material(name='fuel_3_5', material_id=53) 
fuel_3_5.add_macroscopic('fuel_3_5') 
fuel_3_6 = openmc.Material(name='fuel_3_6', material_id=54) 
fuel_3_6.add_macroscopic('fuel_3_6') 
fuel_3_7 = openmc.Material(name='fuel_3_7', material_id=55) 
fuel_3_7.add_macroscopic('fuel_3_7') 
fuel_3_8 = openmc.Material(name='fuel_3_8', material_id=56) 
fuel_3_8.add_macroscopic('fuel_3_8') 
fuel_3_9 = openmc.Material(name='fuel_3_9', material_id=57) 
fuel_3_9.add_macroscopic('fuel_3_9') 
fuel_3_10 = openmc.Material(name='fuel_3_10', material_id=58) 
fuel_3_10.add_macroscopic('fuel_3_10') 
fuel_3_11 = openmc.Material(name='fuel_3_11', material_id=59) 
fuel_3_11.add_macroscopic('fuel_3_11') 
fuel_3_12 = openmc.Material(name='fuel_3_12', material_id=60) 
fuel_3_12.add_macroscopic('fuel_3_12') 

mats = openmc.Materials(
    (
        outer_flibe, 
        graphite_structure, 
        spacers, 
        slot_flibe, 
        inner_flibe_1, 
        inner_flibe_2, 
        inner_flibe_3, 
        P_1_1, 
        P_1_2, 
        P_1_3, 
        P_1_4, 
        P_1_5, 
        P_1_6, 
        P_2_1, 
        P_2_2, 
        P_2_3, 
        P_2_4, 
        P_2_5, 
        P_2_6, 
        P_3_1, 
        P_3_2, 
        P_3_3, 
        P_3_4, 
        P_3_5, 
        P_3_6, 
        fuel_1_1, 
        fuel_1_2, 
        fuel_1_3, 
        fuel_1_4, 
        fuel_1_5, 
        fuel_1_6, 
        fuel_1_7, 
        fuel_1_8, 
        fuel_1_9, 
        fuel_1_10, 
        fuel_1_11, 
        fuel_1_12, 
        fuel_2_1, 
        fuel_2_2, 
        fuel_2_3, 
        fuel_2_4, 
        fuel_2_5, 
        fuel_2_6, 
        fuel_2_7, 
        fuel_2_8, 
        fuel_2_9, 
        fuel_2_10, 
        fuel_2_11, 
        fuel_2_12, 
        fuel_3_1, 
        fuel_3_2, 
        fuel_3_3, 
        fuel_3_4, 
        fuel_3_5, 
        fuel_3_6, 
        fuel_3_7, 
        fuel_3_8, 
        fuel_3_9, 
        fuel_3_10, 
        fuel_3_11, 
        fuel_3_12, 
    )
)
mats.cross_sections = "mgxs.h5"

# top and bottom surfaces (dz)
z_thickness = 21
top_surface = openmc.ZPlane(
    z0=T_pitch / 2 + (z_thickness - 1) / 2 * T_pitch, boundary_type='reflective')
bot_surface = openmc.ZPlane(
    z0=-(T_pitch / 2 + (z_thickness - 1) / 2 * T_pitch), boundary_type='reflective')

# Outermost Hexagon
H_m = 1 / tan(pi / 6)
H_1 = openmc.YPlane(0.5 * H_side_big / tan(pi / 6), 'reflective')
H_2 = plane(-H_m, 0.5 * H_side_big, 0.5 * H_side_big / tan(pi / 6), 'reflective')
H_3 = plane(H_m, 0.5 * H_side_big, -0.5 * H_side_big / tan(pi / 6), 'reflective')
H_4 = openmc.YPlane(-0.5 * H_side_big / tan(pi / 6), 'reflective')
H_5 = plane(-H_m, -0.5 * H_side_big, -0.5 * H_side_big / tan(pi / 6),
            'reflective')
H_6 = plane(H_m, -0.5 * H_side_big, 0.5 * H_side_big / tan(pi / 6), 'reflective')
#H_1.periodic_surface = H_4
#H_2.periodic_surface = H_5
#H_3.periodic_surface = H_6
H_region = -H_1 & +H_4 & -H_2 & +H_3 & +H_5 & -H_6
H_cell = openmc.Cell(fill=outer_flibe, cell_id=1)
H_cell.region = H_region & -top_surface & + bot_surface

# Inner Hexagon
Hi_1 = openmc.YPlane(0.5 * H_side / tan(pi / 6))
Hi_2 = plane(-H_m, 0.5 * H_side, 0.5 * H_side / tan(pi / 6))
Hi_3 = plane(H_m, 0.5 * H_side, -0.5 * H_side / tan(pi / 6))
Hi_4 = openmc.YPlane(-0.5 * H_side / tan(pi / 6))
Hi_5 = plane(-H_m, -0.5 * H_side, -0.5 * H_side / tan(pi / 6))
Hi_6 = plane(H_m, -0.5 * H_side, 0.5 * H_side / tan(pi / 6))
Hi_region = -Hi_1 & +Hi_4 & -Hi_2 & +Hi_3 & +Hi_5 & -Hi_6
Hi_cell = openmc.Cell(fill=graphite_structure, cell_id=2)
Hi_cell.region = Hi_region & -top_surface & + bot_surface
H_cell.region &= ~Hi_region

# Diamond Plank Area
D_cells = []
A1_D_cell = openmc.Cell(fill=inner_flibe_1, cell_id=3)
A1_D_cell.region = region_maker('A1', 'D') & -top_surface & + bot_surface

A2_D_cell = openmc.Cell(fill=inner_flibe_2, cell_id=4)
A2_D_cell.region = region_maker('A2', 'D') & -top_surface & + bot_surface

A3_D_cell = openmc.Cell(fill=inner_flibe_3, cell_id=5)
A3_D_cell.region = region_maker('A3', 'D') & -top_surface & + bot_surface

D_cells = [A1_D_cell, A2_D_cell, A3_D_cell]
for cell in D_cells:
    Hi_cell.region &= ~cell.region
    #H_cell.region &= ~cell.region

# Graphite Planks
P_material = {1: {1: P_1_1, 2: P_1_2, 3:P_1_3, 4:P_1_4, 5:P_1_5, 6:P_1_6},
              2: {1: P_2_1, 2: P_2_2, 3:P_2_3, 4:P_2_4, 5:P_2_5, 6:P_2_6},
              3: {1: P_3_1, 2: P_3_2, 3:P_3_3, 4:P_3_4, 5:P_3_5, 6:P_3_6},}
P_cells = []
count = 100
for area in range(3):
    area_str = 'A{}'.format(area + 1)
    P_region = region_maker(area_str, 'P')
    for trans in range(6):
        P_cell = openmc.Cell(fill=P_material[area+1][trans+1], region=P_region)
        P_univ = openmc.Universe(cells=(P_cell,))
        P_region_new = P_region.translate((trans * T[area_str]['P']['x'], trans * T[area_str]['P']['y'], 0)) & - top_surface & + bot_surface
        P_cell_new = openmc.Cell(fill=P_univ, region=P_region_new, cell_id=count)
        count += 1
        P_cell_new.translation = (
            trans *
            T[area_str]['P']['x'],
            trans *
            T[area_str]['P']['y'],
            0)
        P_cells.append(P_cell_new)
        for cell in D_cells:
            cell.region &= ~P_region_new
        Hi_cell.region &= ~P_region_new
        #H_cell.region &= ~P_region_new

# Fuel Plank
F_material = {1: {1: fuel_1_1, 2: fuel_1_2, 3: fuel_1_3, 4: fuel_1_4, 5: fuel_1_5, 6: fuel_1_6, 
                  7: fuel_1_7, 8: fuel_1_8, 9: fuel_1_9, 10: fuel_1_10, 11: fuel_1_11, 12: fuel_1_12},
              2: {1: fuel_2_1, 2: fuel_2_2, 3: fuel_2_3, 4: fuel_2_4, 5: fuel_2_5, 6: fuel_2_6, 
                  7: fuel_2_7, 8: fuel_2_8, 9: fuel_2_9, 10: fuel_2_10, 11: fuel_2_11, 12: fuel_2_12},
              3: {1: fuel_3_1, 2: fuel_3_2, 3: fuel_3_3, 4: fuel_3_4, 5: fuel_3_5, 6: fuel_3_6, 
                  7: fuel_3_7, 8: fuel_3_8, 9: fuel_3_9, 10: fuel_3_10, 11: fuel_3_11, 12: fuel_3_12}}
F_cells = []
count = 200
for area in range(3):
    area_str = 'A{}'.format(area + 1)
    F_region = region_maker(area_str, 'F')
    num = 0
    for t in range(6):
        num += 1
        for x in range(2):
            if x > 0:
                num += 1
            F_cell = openmc.Cell()
            F_cell.fill = F_material[area+1][num]
            F_univ = openmc.Universe(cells=(F_cell,))
            x_trans = t * T[area_str]['P']['x']
            y_trans = t * T[area_str]['P']['y']
            if x == 1:
                x_trans += T[area_str]['F']['x']
                y_trans += T[area_str]['F']['y']
            F_region_new = F_region.translate((x_trans, y_trans, 0)) & -top_surface & +bot_surface
            F_cell_new = openmc.Cell(fill=F_univ, region=F_region_new, cell_id=count)
            count += 1
            if area == 1:
                F_cell_new.rotation = (0, 0, -120)
            if area == 2:
                F_cell_new.rotation = (0, 0, 120)
            F_cell_new.translation = (x_trans, y_trans, 0)
            F_cells.append(F_cell_new)
            P_cells[area*6+t].region &= ~F_region_new
            D_cells[area].region &= ~F_region_new
            #for cell in P_cells:
            #    cell.region &= ~F_region_new
            #for cell in D_cells:
            #    cell.region &= ~F_region_new
            Hi_cell.region &= ~F_region_new
            #H_cell.region &= ~F_region_new

# Spacer

all_S_univ = openmc.Universe()
S_small_spacer_surf = openmc.ZCylinder(
    r=S_small_r,
    x0=-D_to_center_width - S_A1_D_gap,
    y0=-D_to_center - P_small_gap)  # initialize
all_S_regions = -S_small_spacer_surf & + \
    plane(V['A1']['P']['T']['m'], V['A1']['P']['T']['x'], V['A1']['P']['T']['y'])

# outer loop is for 3 types of spacers, small top, big middle, small bottom
rad = [S_small_r, S_large_r, S_small_r]
start = [0, 1, 5]
end = [1, 6, 6]
C = ['C', 'C', 'Cb']
for y in range(3):
    for area in range(3):
        area_str = 'A{}'.format(area + 1)
        S_cylinder = openmc.ZCylinder(r=rad[y],
                                      x0=V[area_str]['S'][C[y]]['x0'],
                                      y0=V[area_str]['S'][C[y]]['y0'])
        if area == 0:
            S_region = -S_cylinder & + \
                plane(V[area_str]['P']['T']['m'], V[area_str]['P']['T']['x'], V[area_str]['P']['T']['y'])
            if y == 2:
                S_region = -S_cylinder & - \
                    plane(V[area_str]['P']['B']['m'], V[area_str]['P']['B']['x'], V[area_str]['P']['B']['y'])
        if area == 1:
            S_region = -S_cylinder & - \
                plane(V[area_str]['P']['R']['m'], V[area_str]['P']['R']['x'], V[area_str]['P']['R']['y'])
            if y == 2:
                S_region = -S_cylinder & + \
                    plane(V[area_str]['P']['L']['m'], V[area_str]['P']['L']['x'], V[area_str]['P']['L']['y'])
        if area == 2:
            S_region = -S_cylinder & - \
                plane(V[area_str]['P']['L']['m'], V[area_str]['P']['L']['x'], V[area_str]['P']['L']['y'])
            if y == 2:
                S_region = -S_cylinder & + \
                    plane(V[area_str]['P']['R']['m'], V[area_str]['P']['R']['x'], V[area_str]['P']['R']['y'])
        S_cell = openmc.Cell(fill=spacers, region=S_region)
        S_univ = openmc.Universe(cells=(S_cell,))
        for trans in range(start[y], end[y]):
            for x in range(2):
                x_trans = trans * T[area_str]['P']['x']
                y_trans = trans * T[area_str]['P']['y']
                if x == 1:
                    x_trans += T[area_str]['S']['x']
                    y_trans += T[area_str]['S']['y']
                S_region_new = S_region.translate((x_trans, y_trans, 0))
                S_cell_new = openmc.Cell(fill=S_univ, region=S_region_new)
                S_cell_new.translation = (x_trans, y_trans, 0)
                all_S_univ.add_cell(S_cell_new)
                all_S_regions |= S_region_new
                #for cell in F_cells:
                #    cell.region &= ~S_region_new
                #for cell in P_cells:
                #    cell.region &= ~S_region_new
                D_cells[y].region &= ~S_region_new
                #for cell in D_cells:
                #    cell.region &= ~S_region_new
                Hi_cell.region &= ~S_region_new
                #H_cell.region &= ~S_region_new
S_areas = openmc.Cell(
    fill=all_S_univ,
    cell_id=400,
    region=all_S_regions & -
    top_surface & +
    bot_surface)

# Control Rod Slot
A1_CS_cell = openmc.Cell(fill=slot_flibe)
A1_CS_cell.region = region_maker('A1', 'CS') & -top_surface & + bot_surface

A2_CS_cell = openmc.Cell(fill=slot_flibe)
A2_CS_cell.region = region_maker('A2', 'CS') & -top_surface & + bot_surface

A3_CS_cell = openmc.Cell(fill=slot_flibe)
A3_CS_cell.region = region_maker('A3', 'CS') & -top_surface & + bot_surface

CS_regions = A1_CS_cell.region | A2_CS_cell.region | A3_CS_cell.region
CS_universe = openmc.Universe(cells=(A1_CS_cell, A2_CS_cell, A3_CS_cell,))
CS_areas = openmc.Cell(fill=CS_universe, region=CS_regions, cell_id=500)
S_areas.region &= ~CS_regions
#for cell in F_cells:
#    cell.region &= ~S_region_new
#for cell in P_cells:
#    cell.region &= ~S_region_new
#for cell in D_cells:
#    cell.region &= ~S_region_new
Hi_cell.region &= ~CS_regions
#H_cell.region &= ~CS_regions

universe = openmc.Universe(
    cells=[
    H_cell,
    Hi_cell,
    S_areas,
    CS_areas] + D_cells + P_cells +F_cells)

geom = openmc.Geometry(universe)

mats.export_to_xml()
geom.export_to_xml()
settings = openmc.Settings()
point = openmc.stats.Point((20, 10, 0))
src = openmc.Source(space=point)
settings.source = src
settings.batches = 80
settings.inactive = 20
settings.particles = 8000
settings.temperature = {'multipole': True, 'method': 'interpolation'}
settings.energy_mode = "multi-group"
settings.export_to_xml()