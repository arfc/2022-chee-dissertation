import openmc
import sys
import numpy as np
from numpy import sin, cos, tan, pi
sys.path.insert(1, '/Users/gwenchee/github/fhr-benchmark-1/scripts')
import phase1a_constants as pc  # noqa

uoc_9 = openmc.Material()
uoc_9.set_density('atom/b-cm', 7.038386E-2)
uoc_9.add_nuclide('U235', 2.27325e-3)
uoc_9.add_nuclide('U238', 2.269476e-2)
uoc_9.add_nuclide('O16', 3.561871e-2)
uoc_9.add_nuclide('C0', 9.79714e-3)
uoc_9.temperature = 1024

graphite = openmc.Material()
graphite.set_density('g/cc', 1.8)
graphite.add_nuclide('C0', 9.025164e-2)
graphite.add_s_alpha_beta('c_Graphite')
graphite.temperature = 1024

p_graphite = openmc.Material()
p_graphite.set_density('g/cc', 1.8)
p_graphite.add_nuclide('C0', 9.025164e-2)
p_graphite.add_s_alpha_beta('c_Graphite')
p_graphite.temperature = 1024

flibe = openmc.Material()
flibe.set_density('atom/b-cm', 8.30097E-2)
flibe.add_nuclide('Li6', 1.383014e-6)
flibe.add_nuclide('Li7', 2.37132e-2)
flibe.add_nuclide('Be9', 1.18573e-2)
flibe.add_nuclide('F19', 4.74291e-2)
flibe.temperature = 1024

triso_4_layers = openmc.Material()
triso_4_layers.add_nuclide("C0", 0.06851594519357823)
triso_4_layers.add_nuclide("Si28", 0.009418744960032735)
triso_4_layers.add_nuclide("Si29", 0.00048013017638108395)
triso_4_layers.add_nuclide("Si30", 0.0003166830980933728)
triso_4_layers.set_density("sum")

mats = openmc.Materials(
    (uoc_9,
     graphite,
     p_graphite,
     flibe,
     triso_4_layers))

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
H_cell = openmc.Cell(fill=flibe, cell_id=1001)
H_cell.region = H_region & -top_surface & + bot_surface

# inner hexagon
Hi_half_point = 0.5 * pc.H_side / tan(pi / 6)
Hi_half_point_adj = pc.H_side * cos(pi/3)
flibe_thickness = H_half_point - Hi_half_point
flibe_thickness_hyp = flibe_thickness / sin(pi / 3)

Hi_bot = openmc.YPlane(y0=flibe_thickness)
Hi_left = pc.plane(m=-H_m, x=flibe_thickness_hyp, y=H_half_point)

Hi_region = + Hi_bot & -H_top & +Hi_left & -H_right
Hi_cell = openmc.Cell(fill=graphite, cell_id=1002)
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
D_cell = openmc.Cell(fill=flibe, cell_id=1003)
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
CS_cell = openmc.Cell(fill=flibe, cell_id=1004)
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
for i in range(6):
    P_top = openmc.YPlane(y0=P_starting_point - i * P_cell_height_width)
    P_bot = openmc.YPlane(
        y0=P_starting_point -
        pc.P_A1_height -
        i *
        P_cell_height_width)
    P_cell = openmc.Cell(fill=p_graphite, cell_id=1005 + i)
    P_cell.region = -P_top & +P_bot & +P_left & - \
        P_right & -top_surface & + bot_surface
    P_cells.append(P_cell)
    D_cell.region &= ~P_cell.region
    Hi_cell.region &= ~P_cell.region

F_cell_width = (pc.F_len + pc.F_F_gap_adj) / 10
F_cell_height = 1.85
F_starting_point = pc.H_side_big - pc.D_to_center_width - pc.F_len - 1 * pc.F_A1_D_gap


def triso_distr(
        total_pf,
        sine_a_x,
        sine_b_x,
        sine_c_x,
        sine_a_y,
        sine_b_y,
        sine_c_y,
        constant=False):
    if constant:
        pf_distr = [[total_pf]*10]*6
    else:
        midpoints_discr_x = np.arange(
            F_starting_point + F_cell_width / 2,
            F_starting_point + pc.F_len + pc.F_F_gap_adj,
            F_cell_width)
        sine_val_discr_x = sine_a_x * \
            sin(sine_b_x * midpoints_discr_x + sine_c_x) + 2
        midpoints_discr_y = np.arange(P_starting_point -
                                    pc.P_A1_height /
                                    2, P_starting_point -
                                    pc.D_A1_height, -
                                    P_cell_height_width)
        sine_val_discr_y = sine_a_y * \
            sin(sine_b_y * midpoints_discr_y + sine_c_y) + 2
        sine_val_distr_xy = sine_val_discr_y.reshape(
            6, 1) * sine_val_discr_x.reshape(1, 10)
        vol_triso = 4 / 3 * pi * pc.T_r5 ** 3
        vol_total = F_cell_width * 10 * F_cell_height * pc.T_pitch * \
            20 * 6  # length * width * height * no_planks
        vol_slice = F_cell_width * 1 * F_cell_height * pc.T_pitch * \
            20  # length * width * height * no_planks
        no_trisos = total_pf * vol_total / vol_triso
        triso_distr = sine_val_distr_xy / sum(sum(sine_val_distr_xy)) * no_trisos
        pf_distr = triso_distr * vol_triso / vol_slice
    return pf_distr


# 4 layer triso
two_spheres = [openmc.Sphere(r=r) for r in [pc.T_r1, pc.T_r5]]
two_triso_cells = [
    openmc.Cell(fill=uoc_9, region=-two_spheres[0]),
    openmc.Cell(fill=triso_4_layers, region=+two_spheres[0] & -two_spheres[1]),
    openmc.Cell(fill=p_graphite, region=+two_spheres[1])]
two_triso_univ = openmc.Universe(cells=two_triso_cells)
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
            try:
                centers = openmc.model.pack_spheres(
                    radius=pc.T_r5, region=F_cell_region, pf=pf)
                trisos = [
                    openmc.model.TRISO(
                        pc.T_r5,
                        two_triso_univ,
                        c) for c in centers]
                F_cell = openmc.Cell(
                    region=F_cell_region,
                    name="F_cell_"+str(count),
                    cell_id= 5000+count* 10000)
                lower_left, upper_right = F_cell_region.bounding_box
                shape = tuple(((upper_right - lower_left) / 0.4).astype(int))
                pitch = (upper_right - lower_left) / shape
                lattice = openmc.model.create_triso_lattice(
                    trisos, lower_left, pitch, shape, p_graphite
                )
                F_cell.fill = lattice
            except BaseException:
                F_cell = openmc.Cell(
                    fill=p_graphite,
                    region=F_cell_region,
                    name="F_cell_"+str(count),
                    cell_id= 5000+count* 10000)
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

plot = openmc.Plot()
plot.basis = "xy"
plot.origin = (20, 12, 0)
plot.width = (42, 30)
plot.pixels = (1000, 715)
colors = {
    uoc_9: "black",
    graphite: "grey",
    flibe: "blue",
    p_graphite: "red",
    triso_4_layers: "black",
}
plot.color_by = "material"
plot.colors = colors
plots = openmc.Plots()
plots.append(plot)
