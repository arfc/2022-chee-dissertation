import openmc
import numpy as np
from numpy import sin, cos, tan, pi
import sys
sys.path.insert(1, '../../../../fhr-benchmark-1/scripts/')
from phase1a_constants import *
from tallies import *
sys.path.insert(1, '../../../../moltres/python')
from moltres_xs import *  # noqa: E402

###############################################################################
#                 Exporting to OpenMC materials.xml file
###############################################################################

uoc_9 = openmc.Material()
uoc_9.set_density('atom/b-cm', 7.038386E-2)
uoc_9.add_nuclide('U235', 2.27325e-3)
uoc_9.add_nuclide('U238', 2.269476e-2)
uoc_9.add_nuclide('O16', 3.561871e-2)
uoc_9.add_nuclide('C0', 9.79714e-3)
uoc_9.temperature = 948
uoc_9.volume = 4 / 3 * pi * (T_r1 ** 3) * 101 * 210 * 4 * 36
uoc_9.depletable = True

por_c = openmc.Material()
por_c.set_density('atom/b-cm', 5.013980E-2)
por_c.add_nuclide('C0', 5.013980e-2)
por_c.temperature = 948

si_c = openmc.Material()
si_c.set_density('atom/b-cm', 9.612234E-2)
si_c.add_nuclide('Si28', 4.431240e-2)
si_c.add_nuclide('Si29', 2.25887e-3)
si_c.add_nuclide('Si30', 1.48990e-3)
si_c.add_nuclide('C0', 4.806117e-2)
si_c.temperature = 948

graphite = openmc.Material()
graphite.set_density('g/cc', 1.8)
graphite.add_nuclide('C0', 9.025164e-2)
graphite.add_s_alpha_beta('c_Graphite')
graphite.temperature = 948

p_graphite = openmc.Material()
p_graphite.set_density('g/cc', 1.8)
p_graphite.add_nuclide('C0', 9.025164e-2)
p_graphite.add_s_alpha_beta('c_Graphite')
p_graphite.temperature = 948

s_graphite = openmc.Material()
s_graphite.set_density('g/cc', 1.8)
s_graphite.add_nuclide('C0', 9.025164e-2)
s_graphite.add_s_alpha_beta('c_Graphite')
s_graphite.temperature = 948

lm_graphite = openmc.Material()
lm_graphite.set_density('g/cc', 1.8)
lm_graphite.add_nuclide('C0', 9.025164e-2)
lm_graphite.add_s_alpha_beta('c_Graphite')
lm_graphite.temperature = 948

flibe = openmc.Material()
flibe.set_density('atom/b-cm', 8.30097E-2)
flibe.add_nuclide('Li6', 1.383014e-6)
flibe.add_nuclide('Li7', 2.37132e-2)
flibe.add_nuclide('Be9', 1.18573e-2)
flibe.add_nuclide('F19', 4.74291e-2)
flibe.temperature = 948

mats = openmc.Materials(
    (uoc_9,
     por_c,
     si_c,
     graphite,
     p_graphite,
     lm_graphite,
     flibe,
     s_graphite))
mats.export_to_xml()

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
H_region = -H_1 & +H_4 & -H_2 & +H_3 & +H_5 & -H_6
H_cell = openmc.Cell(fill=flibe, cell_id=1)
H_cell.region = H_region & -top_surface & + bot_surface

# Inner Hexagon
Hi_1 = openmc.YPlane(0.5 * H_side / tan(pi / 6))
Hi_2 = plane(-H_m, 0.5 * H_side, 0.5 * H_side / tan(pi / 6))
Hi_3 = plane(H_m, 0.5 * H_side, -0.5 * H_side / tan(pi / 6))
Hi_4 = openmc.YPlane(-0.5 * H_side / tan(pi / 6))
Hi_5 = plane(-H_m, -0.5 * H_side, -0.5 * H_side / tan(pi / 6))
Hi_6 = plane(H_m, -0.5 * H_side, 0.5 * H_side / tan(pi / 6))
Hi_region = -Hi_1 & +Hi_4 & -Hi_2 & +Hi_3 & +Hi_5 & -Hi_6
Hi_cell = openmc.Cell(fill=graphite, cell_id=2)
Hi_cell.region = Hi_region & -top_surface & + bot_surface
H_cell.region &= ~Hi_region

# Diamond Plank Area
D_cells = []
A1_D_cell = openmc.Cell(fill=flibe, cell_id=3)
A1_D_cell.region = region_maker('A1', 'D') & -top_surface & + bot_surface

A2_D_cell = openmc.Cell(fill=flibe, cell_id=4)
A2_D_cell.region = region_maker('A2', 'D') & -top_surface & + bot_surface

A3_D_cell = openmc.Cell(fill=flibe, cell_id=5)
A3_D_cell.region = region_maker('A3', 'D') & -top_surface & + bot_surface

D_cells = [A1_D_cell, A2_D_cell, A3_D_cell]
for cell in D_cells:
    Hi_cell.region &= ~cell.region
    #H_cell.region &= ~cell.region

# Graphite Planks
P_cells = []
count = 100
for area in range(3):
    area_str = 'A{}'.format(area + 1)
    P_region = region_maker(area_str, 'P')
    P_cell = openmc.Cell(fill=p_graphite, region=P_region)
    P_univ = openmc.Universe(cells=(P_cell,))
    for trans in range(6):
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

# Triso Particles
spheres = [openmc.Sphere(r=r)
           for r in [T_r1, T_r2, T_r3, T_r4, T_r5]]
triso_cells = [openmc.Cell(fill=uoc_9, region=-spheres[0]),
               openmc.Cell(fill=por_c, region=+spheres[0] & -spheres[1]),
               openmc.Cell(fill=graphite, region=+spheres[1] & -spheres[2]),
               openmc.Cell(fill=si_c, region=+spheres[2] & -spheres[3]),
               openmc.Cell(fill=graphite, region=+spheres[3] & -spheres[4]),
               openmc.Cell(fill=lm_graphite, region=+spheres[4])]
triso_univ = openmc.Universe(cells=triso_cells)
lm_graphite_cell = openmc.Cell(fill=lm_graphite)
lm_graphite_univ = openmc.Universe(cells=(lm_graphite_cell,))

u = triso_univ
lattice = openmc.RectLattice()
lattice.lower_left = (V['A1']['F']['L']['x'], V['A1']['F']['B']
                      ['y'], -(T_pitch / 2 + (z_thickness - 1) / 2 * T_pitch))
lattice.pitch = (T_pitch, T_pitch, T_pitch)
lattice.outer = lm_graphite_univ
lattice_list = []
for z in range(z_thickness):
    lattice_z_list = []
    for row in range(4):
        lattice_y_list = []
        for col in range(210):
            lattice_y_list.append(u)
        lattice_z_list.append(lattice_y_list)
    lattice_list.append(lattice_z_list)
lattice.universes = lattice_list

# Fuel Plank
F_cells = []
count = 200
for area in range(3):
    area_str = 'A{}'.format(area + 1)
    F_region = region_maker(area_str, 'F')
    F_cell = openmc.Cell(fill=lm_graphite,)
    F_cell.fill = lattice
    F_univ = openmc.Universe(cells=(F_cell,))
    for t in range(6):
        for x in range(2):
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
        S_cell = openmc.Cell(fill=s_graphite, region=S_region)
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
A1_CS_cell = openmc.Cell(fill=flibe)
A1_CS_cell.region = region_maker('A1', 'CS') & -top_surface & + bot_surface

A2_CS_cell = openmc.Cell(fill=flibe)
A2_CS_cell.region = region_maker('A2', 'CS') & -top_surface & + bot_surface

A3_CS_cell = openmc.Cell(fill=flibe)
A3_CS_cell.region = region_maker('A3', 'CS') & -top_surface & + bot_surface

CS_regions = A1_CS_cell.region | A2_CS_cell.region | A3_CS_cell.region
CS_universe = openmc.Universe(cells=(A1_CS_cell, A2_CS_cell, A3_CS_cell,))
CS_areas = openmc.Cell(fill=CS_universe, region=CS_regions, cell_id=500)
S_areas.region &= ~CS_regions
Hi_cell.region &= ~CS_regions

universe = openmc.Universe(
    cells=[
    H_cell,
    Hi_cell,
    S_areas,
    CS_areas] + D_cells + P_cells +F_cells)

# tallies 
tallies_file = openmc.Tallies()

# Comparison key neutronics parameters 
# beta
beta_mesh = openmc.RegularMesh()
beta_mesh.dimension = [1, 1]
Lx, Ly = 27.1, 23.4
beta_mesh.lower_left = [-Lx, -Ly]
beta_mesh.upper_right = [Lx, Ly]
beta_mesh_filter = openmc.MeshFilter(beta_mesh)
beta_tally = openmc.Tally(name='beta')
beta_tally.filters = [beta_mesh_filter]
beta_tally.scores = ['delayed-nu-fission', 'nu-fission']
tallies_file.append(beta_tally, merge=True)

# flux 
energy_filter = openmc.EnergyFilter([1e-6, 1.8554, 2.9023e1, 9.1188e3, 2.0e7])
mesh_flux = openmc.RegularMesh()
mesh_flux.dimension = [100, 1000]
mesh_flux.lower_left = [-Lx, -Ly]
mesh_flux.upper_right = [Lx, Ly]
mesh_filter_flux = openmc.MeshFilter(mesh_flux)
tally_flux = openmc.Tally(name='flux')
tally_flux.filters = [mesh_filter_flux, energy_filter]
tally_flux.scores = [
    'flux',
    'nu-fission',
    'fission',]
tallies_file.append(tally_flux)

# spectrum 
# 252 energy groups
engs = [1.00E-11, 1.00E-10, 5.00E-10, 7.50E-10, 1.00E-09, 1.20E-09,
        1.50E-09, 2.00E-09, 2.50E-09, 3.00E-09, 4.00E-09, 5.00E-09,
        7.50E-09, 1.00E-08, 2.53E-08, 3.00E-08, 4.00E-08, 5.00E-08,
        6.00E-08, 7.00E-08, 8.00E-08, 9.00E-08, 1.00E-07, 1.25E-07,
        1.50E-07, 1.75E-07, 2.00E-07, 2.25E-07, 2.50E-07, 2.75E-07,
        3.00E-07, 3.25E-07, 3.50E-07, 3.75E-07, 4.00E-07, 4.50E-07,
        5.00E-07, 5.50E-07, 6.00E-07, 6.25E-07, 6.50E-07, 7.00E-07,
        7.50E-07, 8.00E-07, 8.50E-07, 9.00E-07, 9.25E-07, 9.50E-07,
        9.75E-07, 1.00E-06, 1.01E-06, 1.02E-06, 1.03E-06, 1.04E-06,
        1.05E-06, 1.06E-06, 1.07E-06, 1.08E-06, 1.09E-06, 1.10E-06,
        1.11E-06, 1.12E-06, 1.13E-06, 1.14E-06, 1.15E-06, 1.18E-06,
        1.20E-06, 1.23E-06, 1.25E-06, 1.30E-06, 1.35E-06, 1.40E-06,
        1.45E-06, 1.50E-06, 1.59E-06, 1.68E-06, 1.77E-06, 1.86E-06,
        1.94E-06, 2.00E-06, 2.12E-06, 2.21E-06, 2.30E-06, 2.38E-06,
        2.47E-06, 2.57E-06, 2.67E-06, 2.77E-06, 2.87E-06, 2.97E-06,
        3.00E-06, 3.10E-06, 3.20E-06, 3.50E-06, 3.73E-06, 4.10E-06,
        4.70E-06, 5.00E-06, 5.40E-06, 6.00E-06, 6.25E-06, 6.50E-06,
        6.75E-06, 6.88E-06, 7.00E-06, 7.15E-06, 8.10E-06, 9.10E-06,
        1.00E-05, 1.15E-05, 1.19E-05, 1.29E-05, 1.44E-05, 1.60E-05,
        1.70E-05, 1.85E-05, 1.94E-05, 2.00E-05, 2.05E-05, 2.12E-05,
        2.18E-05, 2.25E-05, 2.50E-05, 2.75E-05, 3.00E-05, 3.13E-05,
        3.18E-05, 3.33E-05, 3.38E-05, 3.50E-05, 3.55E-05, 3.60E-05,
        3.70E-05, 3.71E-05, 3.73E-05, 3.76E-05, 3.80E-05, 3.91E-05,
        3.96E-05, 4.10E-05, 4.24E-05, 4.40E-05, 4.52E-05, 4.83E-05,
        5.06E-05, 5.34E-05, 5.80E-05, 6.10E-05, 6.30E-05, 6.50E-05,
        6.75E-05, 7.20E-05, 7.60E-05, 8.00E-05, 8.17E-05, 9.00E-05,
        9.70E-05, 1.01E-04, 1.05E-04, 1.08E-04, 1.13E-04, 1.16E-04,
        1.18E-04, 1.19E-04, 1.22E-04, 1.43E-04, 1.70E-04, 1.80E-04,
        1.88E-04, 1.89E-04, 1.92E-04, 1.93E-04, 2.02E-04, 2.07E-04,
        2.10E-04, 2.20E-04, 2.40E-04, 2.85E-04, 3.05E-04, 5.50E-04,
        6.70E-04, 6.83E-04, 9.50E-04, 1.15E-03, 1.50E-03, 1.55E-03,
        1.80E-03, 2.20E-03, 2.25E-03, 2.50E-03, 3.00E-03, 3.74E-03,
        3.90E-03, 5.70E-03, 8.03E-03, 9.50E-03, 1.30E-02, 1.70E-02,
        2.00E-02, 3.00E-02, 4.50E-02, 5.00E-02, 5.20E-02, 6.00E-02,
        7.30E-02, 7.50E-02, 8.20E-02, 8.50E-02, 1.00E-01, 1.28E-01,
        1.49E-01, 2.00E-01, 2.70E-01, 3.30E-01, 4.00E-01, 4.20E-01,
        4.40E-01, 4.70E-01, 4.92E-01, 5.50E-01, 5.73E-01, 6.00E-01,
        6.70E-01, 6.79E-01, 7.50E-01, 8.20E-01, 8.61E-01, 8.75E-01,
        9.00E-01, 9.20E-01, 1.01E+00, 1.10E+00, 1.20E+00, 1.25E+00,
        1.32E+00, 1.36E+00, 1.40E+00, 1.50E+00, 1.85E+00, 2.35E+00,
        2.48E+00, 3.00E+00, 4.30E+00, 4.80E+00, 6.43E+00, 8.19E+00,
        1.00E+01, 1.28E+01, 1.38E+01, 1.46E+01, 1.57E+01, 1.73E+01,
        2.00E+01]
engs = [x * 1e6 for x in engs]
energy_filter_all = openmc.EnergyFilter(engs)
mesh_spectrum = openmc.RegularMesh()
mesh_spectrum.dimension = [1, 1]
mesh_spectrum.lower_left = [-Lx, -Ly]
mesh_spectrum.upper_right = [Lx, Ly]
mesh_filter_spectrum = openmc.MeshFilter(mesh_spectrum)
tally_spectrum_all = openmc.Tally(name='spectrum all')
tally_spectrum_all.filters = [mesh_filter_spectrum, energy_filter_all]
tally_spectrum_all.scores = ['flux', 'nu-fission', 'fission']
tallies_file.append(tally_spectrum_all)

tally_spectrum_4 = openmc.Tally(name='spectrum 4 groups')
tally_spectrum_4.filters = [mesh_filter_spectrum, energy_filter]
tally_spectrum_4.scores = ['flux', 'nu-fission', 'fission']
tallies_file.append(tally_spectrum_4)

# Moltres group constants 
all_cells = [
    H_cell,
    Hi_cell,
    S_areas,
    CS_areas] + D_cells + P_cells + F_cells
all_cells_id = []
for c in all_cells:
    all_cells_id.append(c.id)
domain_dict = openmc_xs.generate_openmc_tallies_xml(
    [1e-6, 1.8554, 2.9023e1, 9.1188e3, 2.0e7],
    list(range(1, 7)),
    all_cells,
    all_cells_id,
    tallies_file,
)
geom = openmc.Geometry(universe)

# MGXS 
# option 2 cole gentry 
groups = openmc.mgxs.EnergyGroups([1e-6, 1.8554, 2.9023e1, 9.1188e3, 2.0e7])
mgxs_lib = openmc.mgxs.Library(geom)
mgxs_lib.energy_groups = groups
mgxs_lib.domain_type = "cell"
mgxs_lib.domains = all_cells
mgxs_lib.by_nuclide = False
mgxs_lib.mgxs_types = ['total', 'absorption', 'nu-fission', 'fission',
                       'nu-scatter matrix', 'multiplicity matrix', 'chi']
mgxs_lib.legendre_order = 3
mgxs_lib.check_library_for_openmc_mgxs()
mgxs_lib.build_library()

tallies_file = openmc.Tallies()
mgxs_lib.add_to_tallies_file(tallies_file, merge=True)
tallies_file.export_to_xml()

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
settings.export_to_xml()