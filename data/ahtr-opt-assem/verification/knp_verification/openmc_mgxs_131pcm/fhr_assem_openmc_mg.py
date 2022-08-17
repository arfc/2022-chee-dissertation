import openmc
import numpy as np
from numpy import sin, cos, tan, pi
import sys
sys.path.insert(1, '/Users/gwenchee/github/fhr-benchmark-1/scripts/')
import phase1a_constants as pc  # noqa

# materials 
outer_flibe = openmc.Material(name="outer_flibe", material_id=1)
outer_flibe.add_macroscopic("outer_flibe")
graphite_structure = openmc.Material(name="graphite_structure", material_id=2)
graphite_structure.add_macroscopic("graphite_structure")
inner_flibe = openmc.Material(name="inner_flibe", material_id=3)
inner_flibe.add_macroscopic("inner_flibe")
slot_flibe = openmc.Material(name="inner_flibe", material_id=4)
slot_flibe.add_macroscopic("inner_flibe")
P_1 = openmc.Material(name="P_1", material_id=5)
P_1.add_macroscopic("P_1")
P_2 = openmc.Material(name="P_2", material_id=6)
P_2.add_macroscopic("P_2")
P_3 = openmc.Material(name="P_3", material_id=7)
P_3.add_macroscopic("P_3")
P_4 = openmc.Material(name="P_4", material_id=8)
P_4.add_macroscopic("P_4")
P_5 = openmc.Material(name="P_5", material_id=9)
P_5.add_macroscopic("P_5")
P_6 = openmc.Material(name="P_6", material_id=10)
P_6.add_macroscopic("P_6")
fuel_1_1 = openmc.Material(name='fuel_1_1', material_id=11) 
fuel_1_1.add_macroscopic('fuel_1_1') 
fuel_1_2 = openmc.Material(name='fuel_1_2', material_id=12) 
fuel_1_2.add_macroscopic('fuel_1_2') 
fuel_1_3 = openmc.Material(name='fuel_1_3', material_id=13) 
fuel_1_3.add_macroscopic('fuel_1_3') 
fuel_1_4 = openmc.Material(name='fuel_1_4', material_id=14) 
fuel_1_4.add_macroscopic('fuel_1_4') 
fuel_1_5 = openmc.Material(name='fuel_1_5', material_id=15) 
fuel_1_5.add_macroscopic('fuel_1_5') 
fuel_1_6 = openmc.Material(name='fuel_1_6', material_id=16) 
fuel_1_6.add_macroscopic('fuel_1_6') 
fuel_1_7 = openmc.Material(name='fuel_1_7', material_id=17) 
fuel_1_7.add_macroscopic('fuel_1_7') 
fuel_1_8 = openmc.Material(name='fuel_1_8', material_id=18) 
fuel_1_8.add_macroscopic('fuel_1_8') 
fuel_1_9 = openmc.Material(name='fuel_1_9', material_id=19) 
fuel_1_9.add_macroscopic('fuel_1_9') 
fuel_1_10 = openmc.Material(name='fuel_1_10', material_id=20) 
fuel_1_10.add_macroscopic('fuel_1_10') 
fuel_2_1 = openmc.Material(name='fuel_2_1', material_id=21) 
fuel_2_1.add_macroscopic('fuel_2_1') 
fuel_2_2 = openmc.Material(name='fuel_2_2', material_id=22) 
fuel_2_2.add_macroscopic('fuel_2_2') 
fuel_2_3 = openmc.Material(name='fuel_2_3', material_id=23) 
fuel_2_3.add_macroscopic('fuel_2_3') 
fuel_2_4 = openmc.Material(name='fuel_2_4', material_id=24) 
fuel_2_4.add_macroscopic('fuel_2_4') 
fuel_2_5 = openmc.Material(name='fuel_2_5', material_id=25) 
fuel_2_5.add_macroscopic('fuel_2_5') 
fuel_2_6 = openmc.Material(name='fuel_2_6', material_id=26) 
fuel_2_6.add_macroscopic('fuel_2_6') 
fuel_2_7 = openmc.Material(name='fuel_2_7', material_id=27) 
fuel_2_7.add_macroscopic('fuel_2_7') 
fuel_2_8 = openmc.Material(name='fuel_2_8', material_id=28) 
fuel_2_8.add_macroscopic('fuel_2_8') 
fuel_2_9 = openmc.Material(name='fuel_2_9', material_id=29) 
fuel_2_9.add_macroscopic('fuel_2_9') 
fuel_2_10 = openmc.Material(name='fuel_2_10', material_id=30) 
fuel_2_10.add_macroscopic('fuel_2_10') 
fuel_3_1 = openmc.Material(name='fuel_3_1', material_id=31) 
fuel_3_1.add_macroscopic('fuel_3_1') 
fuel_3_2 = openmc.Material(name='fuel_3_2', material_id=32) 
fuel_3_2.add_macroscopic('fuel_3_2') 
fuel_3_3 = openmc.Material(name='fuel_3_3', material_id=33) 
fuel_3_3.add_macroscopic('fuel_3_3') 
fuel_3_4 = openmc.Material(name='fuel_3_4', material_id=34) 
fuel_3_4.add_macroscopic('fuel_3_4') 
fuel_3_5 = openmc.Material(name='fuel_3_5', material_id=35) 
fuel_3_5.add_macroscopic('fuel_3_5') 
fuel_3_6 = openmc.Material(name='fuel_3_6', material_id=36) 
fuel_3_6.add_macroscopic('fuel_3_6') 
fuel_3_7 = openmc.Material(name='fuel_3_7', material_id=37) 
fuel_3_7.add_macroscopic('fuel_3_7') 
fuel_3_8 = openmc.Material(name='fuel_3_8', material_id=38) 
fuel_3_8.add_macroscopic('fuel_3_8') 
fuel_3_9 = openmc.Material(name='fuel_3_9', material_id=39) 
fuel_3_9.add_macroscopic('fuel_3_9') 
fuel_3_10 = openmc.Material(name='fuel_3_10', material_id=40) 
fuel_3_10.add_macroscopic('fuel_3_10') 
fuel_4_1 = openmc.Material(name='fuel_4_1', material_id=41) 
fuel_4_1.add_macroscopic('fuel_4_1') 
fuel_4_2 = openmc.Material(name='fuel_4_2', material_id=42) 
fuel_4_2.add_macroscopic('fuel_4_2') 
fuel_4_3 = openmc.Material(name='fuel_4_3', material_id=43) 
fuel_4_3.add_macroscopic('fuel_4_3') 
fuel_4_4 = openmc.Material(name='fuel_4_4', material_id=44) 
fuel_4_4.add_macroscopic('fuel_4_4') 
fuel_4_5 = openmc.Material(name='fuel_4_5', material_id=45) 
fuel_4_5.add_macroscopic('fuel_4_5') 
fuel_4_6 = openmc.Material(name='fuel_4_6', material_id=46) 
fuel_4_6.add_macroscopic('fuel_4_6') 
fuel_4_7 = openmc.Material(name='fuel_4_7', material_id=47) 
fuel_4_7.add_macroscopic('fuel_4_7') 
fuel_4_8 = openmc.Material(name='fuel_4_8', material_id=48) 
fuel_4_8.add_macroscopic('fuel_4_8') 
fuel_4_9 = openmc.Material(name='fuel_4_9', material_id=49) 
fuel_4_9.add_macroscopic('fuel_4_9') 
fuel_4_10 = openmc.Material(name='fuel_4_10', material_id=50) 
fuel_4_10.add_macroscopic('fuel_4_10') 
fuel_5_1 = openmc.Material(name='fuel_5_1', material_id=51) 
fuel_5_1.add_macroscopic('fuel_5_1') 
fuel_5_2 = openmc.Material(name='fuel_5_2', material_id=52) 
fuel_5_2.add_macroscopic('fuel_5_2') 
fuel_5_3 = openmc.Material(name='fuel_5_3', material_id=53) 
fuel_5_3.add_macroscopic('fuel_5_3') 
fuel_5_4 = openmc.Material(name='fuel_5_4', material_id=54) 
fuel_5_4.add_macroscopic('fuel_5_4') 
fuel_5_5 = openmc.Material(name='fuel_5_5', material_id=55) 
fuel_5_5.add_macroscopic('fuel_5_5') 
fuel_5_6 = openmc.Material(name='fuel_5_6', material_id=56) 
fuel_5_6.add_macroscopic('fuel_5_6') 
fuel_5_7 = openmc.Material(name='fuel_5_7', material_id=57) 
fuel_5_7.add_macroscopic('fuel_5_7') 
fuel_5_8 = openmc.Material(name='fuel_5_8', material_id=58) 
fuel_5_8.add_macroscopic('fuel_5_8') 
fuel_5_9 = openmc.Material(name='fuel_5_9', material_id=59) 
fuel_5_9.add_macroscopic('fuel_5_9') 
fuel_5_10 = openmc.Material(name='fuel_5_10', material_id=60) 
fuel_5_10.add_macroscopic('fuel_5_10') 
fuel_6_1 = openmc.Material(name='fuel_6_1', material_id=61) 
fuel_6_1.add_macroscopic('fuel_6_1') 
fuel_6_2 = openmc.Material(name='fuel_6_2', material_id=62) 
fuel_6_2.add_macroscopic('fuel_6_2') 
fuel_6_3 = openmc.Material(name='fuel_6_3', material_id=63) 
fuel_6_3.add_macroscopic('fuel_6_3') 
fuel_6_4 = openmc.Material(name='fuel_6_4', material_id=64) 
fuel_6_4.add_macroscopic('fuel_6_4') 
fuel_6_5 = openmc.Material(name='fuel_6_5', material_id=65) 
fuel_6_5.add_macroscopic('fuel_6_5') 
fuel_6_6 = openmc.Material(name='fuel_6_6', material_id=66) 
fuel_6_6.add_macroscopic('fuel_6_6') 
fuel_6_7 = openmc.Material(name='fuel_6_7', material_id=67) 
fuel_6_7.add_macroscopic('fuel_6_7') 
fuel_6_8 = openmc.Material(name='fuel_6_8', material_id=68) 
fuel_6_8.add_macroscopic('fuel_6_8') 
fuel_6_9 = openmc.Material(name='fuel_6_9', material_id=69) 
fuel_6_9.add_macroscopic('fuel_6_9') 
fuel_6_10 = openmc.Material(name='fuel_6_10', material_id=70) 
fuel_6_10.add_macroscopic('fuel_6_10') 

mats = openmc.Materials(
    (
        outer_flibe, 
        graphite_structure, 
        inner_flibe,
        slot_flibe,
        P_1, P_2, P_3, P_4, P_5, P_6,
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
        fuel_4_1, 
        fuel_4_2, 
        fuel_4_3, 
        fuel_4_4, 
        fuel_4_5, 
        fuel_4_6, 
        fuel_4_7, 
        fuel_4_8, 
        fuel_4_9, 
        fuel_4_10, 
        fuel_5_1, 
        fuel_5_2, 
        fuel_5_3, 
        fuel_5_4, 
        fuel_5_5, 
        fuel_5_6, 
        fuel_5_7, 
        fuel_5_8, 
        fuel_5_9, 
        fuel_5_10, 
        fuel_6_1, 
        fuel_6_2, 
        fuel_6_3, 
        fuel_6_4, 
        fuel_6_5, 
        fuel_6_6, 
        fuel_6_7, 
        fuel_6_8, 
        fuel_6_9, 
        fuel_6_10
    )
)

mats.cross_sections = "./mgxs.h5"

# z-axis
top_surface = openmc.ZPlane(z0=pc.T_pitch * 10, boundary_type="reflective")
bot_surface = openmc.ZPlane(z0=-pc.T_pitch * 10, boundary_type="reflective")

# outermost flibe
H_m = 1 / tan(pi / 6)
H_half_point = 0.5 * pc.H_side_big / tan(pi / 6)
H_half_point_adj = pc.H_side_big * cos(pi/3)

H_bot = openmc.YPlane(y0=0, boundary_type='reflective')
H_top = openmc.YPlane(y0=H_half_point, boundary_type='reflective')
H_left = pc.plane(m=-H_m, x=0, y=H_half_point, bc='reflective')
H_right = pc.plane(m=-H_m, x=pc.H_side_big, y=H_half_point, bc='reflective')

H_region = +H_bot & -H_top & +H_left & -H_right
H_cell = openmc.Cell(fill=outer_flibe, cell_id=1001)
H_cell.region = H_region & -top_surface & + bot_surface

# inner hexagon
Hi_half_point = 0.5 * pc.H_side / tan(pi / 6)
Hi_half_point_adj = pc.H_side * cos(pi/3)
flibe_thickness = H_half_point - Hi_half_point
flibe_thickness_hyp = flibe_thickness / sin(pi / 3)

Hi_bot = openmc.YPlane(y0=flibe_thickness)
Hi_left = pc.plane(m=-H_m, x=flibe_thickness_hyp, y=H_half_point)

Hi_region = + Hi_bot & -H_top & +Hi_left & -H_right
Hi_cell = openmc.Cell(fill=graphite_structure, cell_id=1002)
Hi_cell.region = Hi_region & -top_surface & + bot_surface
H_cell.region &= ~Hi_region

# Diamond Plank Area
D_bot = openmc.YPlane(y0=H_half_point - pc.D_to_center - pc.D_A1_height)
D_top = openmc.YPlane(y0=H_half_point - pc.D_to_center)
D_left = pc.plane(
    m=-
    H_m,
    x=pc.H_side_big -
    pc.D_to_center_width -
    pc.F_len -
    2 *
    pc.F_A1_D_gap,
    y=H_half_point -
    pc.D_to_center)
D_right = pc.plane(
    m=-
    H_m,
    x=pc.H_side_big -
    pc.D_to_center_width,
    y=H_half_point -
    pc.D_to_center)

D_region = +D_bot & -D_top & +D_left & -D_right
D_cell = openmc.Cell(fill=inner_flibe, cell_id=1003)
D_cell.region = D_region & -top_surface & + bot_surface
Hi_cell.region &= ~D_region

# Control Rod Slot Area
CS_left_left = openmc.XPlane(x0=pc.H_side_big - pc.CS_l)
CS_left_bot = openmc.YPlane(y0=H_half_point - pc.CS_w / 2)
CS_right_left = pc.plane(m=-H_m, x=pc.H_side_big - pc.CS_w / 2 /
                         tan(pi / 3), y=H_half_point - pc.CS_w / 2)
CS_right_bot_m = ((H_half_point - sin(pi / 3) * pc.CS_l + pc.CS_w / 2 * cos(pi / 3)) - (H_half_point - sin(pi / 3) * pc.CS_l)) / \
    ((pc.H_side_big + pc.CS_l * cos(pi / 3) + sin(pi / 3) * pc.CS_w / 2) - (pc.H_side_big + pc.CS_l * cos(pi / 3)))
CS_right_bot = pc.plane(m=CS_right_bot_m,
                        x=pc.H_side_big + pc.CS_l * cos(pi / 3),
                        y=H_half_point - sin(pi / 3) * pc.CS_l)

CS_left_region = +CS_left_left & +CS_left_bot & - \
    H_top & -H_right & -top_surface & + bot_surface

CS_right_region = +CS_right_left & +CS_right_bot & - \
    H_top & -H_right & -top_surface & + bot_surface
CS_cell = openmc.Cell(fill=slot_flibe, cell_id=1004)
CS_cell.region = CS_left_region | CS_right_region
D_cell.region &= ~CS_cell.region
Hi_cell.region &= ~CS_cell.region

# Plank Regions
P_left = pc.plane(
    m=-
    H_m,
    x=pc.H_side_big -
    pc.D_to_center_width -
    pc.F_len -
    2 *
    pc.F_A1_D_gap -
    pc.P_D_jut_hyp,
    y=H_half_point -
    pc.D_to_center)
P_right = pc.plane(m=-
                   H_m, x=pc.H_side_big - pc.D_to_center_width +
                   pc.P_D_jut_hyp, y=H_half_point -
                   pc.D_to_center)
P_cells = []
P_starting_point = H_half_point - pc.D_to_center - pc.P_small_gap
P_cell_height_width = pc.P_A1_height + pc.P_big_gap
P_mats = [P_1, P_2, P_3, P_4, P_5, P_6]
for i in range(6):
    P_top = openmc.YPlane(y0=P_starting_point - i * P_cell_height_width)
    P_bot = openmc.YPlane(
        y0=P_starting_point -
        pc.P_A1_height -
        i *
        P_cell_height_width)
    P_cell = openmc.Cell(fill=P_mats[i], cell_id=1005 + i)
    P_cell.region = -P_top & +P_bot & +P_left & - \
        P_right & -top_surface & + bot_surface
    P_cells.append(P_cell)
    D_cell.region &= ~P_cell.region
    Hi_cell.region &= ~P_cell.region

F_cell_width = (pc.F_len + pc.F_F_gap_adj) / 10
F_cell_height = 1.85
F_starting_point = pc.H_side_big - pc.D_to_center_width - pc.F_len - 1 * pc.F_A1_D_gap

F_mats = [[fuel_1_1, fuel_1_2, fuel_1_3, fuel_1_4, fuel_1_5, fuel_1_6, fuel_1_7, fuel_1_8, fuel_1_9, fuel_1_10],
          [fuel_2_1, fuel_2_2, fuel_2_3, fuel_2_4, fuel_2_5, fuel_2_6, fuel_2_7, fuel_2_8, fuel_2_9, fuel_2_10],
          [fuel_3_1, fuel_3_2, fuel_3_3, fuel_3_4, fuel_3_5, fuel_3_6, fuel_3_7, fuel_3_8, fuel_3_9, fuel_3_10], 
          [fuel_4_1, fuel_4_2, fuel_4_3, fuel_4_4, fuel_4_5, fuel_4_6, fuel_4_7, fuel_4_8, fuel_4_9, fuel_4_10],
          [fuel_5_1, fuel_5_2, fuel_5_3, fuel_5_4, fuel_5_5, fuel_5_6, fuel_5_7, fuel_5_8, fuel_5_9, fuel_5_10],
          [fuel_6_1, fuel_6_2, fuel_6_3, fuel_6_4, fuel_6_5, fuel_6_6, fuel_6_7, fuel_6_8, fuel_6_9, fuel_6_10],]

graphite_thickness = 0.35
first_fuel_cell_bot = H_half_point - pc.D_to_center - \
    pc.P_small_gap - pc.P_A1_height + graphite_thickness
ygap_btwn_fuel_cells = pc.P_A1_height + pc.P_big_gap
xgap_btwn_fuel_cells = (pc.P_A1_height + pc.P_big_gap) / tan(pi / 3)

def create_fuel_cells(pf_distr):
    # Fuel Regions
    F_cells = []
    count = 0
    for j in range(6):
        F_top = openmc.YPlane(y0=H_half_point -
                              pc.D_to_center -
                              pc.P_small_gap -
                              graphite_thickness -
                              j * ygap_btwn_fuel_cells)
        F_bot = openmc.YPlane(y0=first_fuel_cell_bot -
                              j * ygap_btwn_fuel_cells)
        F_i_starting_point = F_starting_point + j * xgap_btwn_fuel_cells
        for i in range(10):
            F_left = openmc.XPlane(x0=F_i_starting_point + i * F_cell_width)
            F_right = openmc.XPlane(
                x0=F_i_starting_point + (i + 1) * F_cell_width)
            F_cell_region = -F_top & +F_bot & +F_left & - \
                F_right & -top_surface & + bot_surface
            pf = pf_distr[j][i]
            F_cell = openmc.Cell(
                region=F_cell_region,
                name="F_cell_"+str(count),
                cell_id= 5000+count* 10000)
            lower_left, upper_right = F_cell_region.bounding_box
            shape = tuple(((upper_right - lower_left) / 0.4).astype(int))
            pitch = (upper_right - lower_left) / shape
            F_cell.fill = F_mats[j][i]
            #F_cell = openmc.Cell(fill=uoc_9, region=F_cell_region, cell_id=5000+count* 10000)
            count += 1
            F_cells.append(F_cell)
            P_cells[j].region &= ~F_cell.region
            D_cell.region &= ~F_cell.region
            Hi_cell.region &= ~F_cell.region
    return F_cells

settings = openmc.Settings()
point = openmc.stats.Point((20, 16, 0))
src = openmc.Source(space=point)
settings.source = src
settings.temperature = {"multipole": True, "method": "interpolation"}
settings.energy_mode = "multi-group"

total_pf = 0.0979

pf_distr = np.array([[total_pf] * 10] * 6)

F_cells = create_fuel_cells(pf_distr)
universe = openmc.Universe(
    cells=[
    H_cell,
    Hi_cell,
    D_cell,
    CS_cell] + P_cells + F_cells)

geom = openmc.Geometry(universe)
settings.batches = 80
settings.inactive = 20
settings.particles = 8000

mats.export_to_xml()
geom.export_to_xml()
settings.export_to_xml()

openmc.run()