import openmc
import numpy as np
from numpy import sin, cos, tan, pi
import sys 
sys.path.insert(1, '../')
from constants import *
sys.path.insert(1, '../../../moltres/python')
from moltres_xs import *  # noqa: E402


uoc_9.temperature = 948
por_c.temperature = 948
si_c.temperature = 948
graphite.temperature = 948
triso_4_layers.temperature = 948
lm_graphite.temperature = 948
flibe.temperature = 948
mats = openmc.Materials((uoc_9, por_c, si_c, graphite, lm_graphite, flibe, triso_4_layers))

# Templating
total_pf = 0.0979
sine_a = 1.989
sine_b = 0.354
sine_c = 3.143
vol_total = 23.1 * 2.55 * T_pitch * 20
vol_slice = 2.31 * 2.55 * T_pitch * 20

x_left = +openmc.XPlane(x0=0, boundary_type="reflective")
x_right = -openmc.XPlane(x0=27.1, boundary_type="reflective")
y_top = -openmc.YPlane(y0=3.25, boundary_type="reflective")
y_bot =  +openmc.YPlane(y0=0, boundary_type="reflective")
z_top = -openmc.ZPlane(z0=T_pitch*20, boundary_type="reflective")
z_bot = +openmc.ZPlane(z0=0, boundary_type="reflective")
bounds = openmc.Cell(fill=flibe)
bounds.region = x_left & x_right & y_top & y_bot & z_top & z_bot

plank_x_left = +openmc.XPlane(x0=2)
plank_x_right = -openmc.XPlane(x0=2+23.1)
plank_y_top = -openmc.YPlane(y0=0.35+2.55)
plank_y_bot = +openmc.YPlane(y0=0.35)
plank_region = plank_x_left & plank_x_right & plank_y_top & plank_y_bot & z_top & z_bot
bounds.region &= ~plank_region

graphite1_x_right = -openmc.XPlane(x0=2)
graphite1 = openmc.Cell(fill=graphite)
graphite1.region = x_left & graphite1_x_right & y_top & y_bot & z_top & z_bot
bounds.region &= ~graphite1.region

graphite2_x_left = +openmc.XPlane(x0=25.1)
graphite2 = openmc.Cell(fill=graphite)
graphite2.region = graphite2_x_left & x_right & y_top & y_bot & z_top & z_bot
bounds.region &= ~graphite2.region

boundaries = np.arange(2,27.1,2.31)
prism_1 = create_prism(boundaries[0], boundaries[1], False, False)
prism_2 = create_prism(boundaries[1], boundaries[2], False, False)
prism_3 = create_prism(boundaries[2], boundaries[3], False, False)
prism_4 = create_prism(boundaries[3], boundaries[4], False, False)
prism_5 = create_prism(boundaries[4], boundaries[5], False, False)
prism_6 = create_prism(boundaries[5], boundaries[6], False, False)
prism_7 = create_prism(boundaries[6], boundaries[7], False, False)
prism_8 = create_prism(boundaries[7], boundaries[8], False, False)
prism_9 = create_prism(boundaries[8], boundaries[9], False, False)
prism_10 = create_prism(boundaries[9], boundaries[10], False, False)

# triso PF distribution
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
print(len(pf_z), pf_z)

prism_cell_1 = create_lattice(prism_1, pf_z[0], 'prism_cell_1', 11)
prism_cell_2 = create_lattice(prism_2, pf_z[1], 'prism_cell_2', 12)
prism_cell_3 = create_lattice(prism_3, pf_z[2], 'prism_cell_3', 13)
prism_cell_4 = create_lattice(prism_4, pf_z[3], 'prism_cell_4', 14)
prism_cell_5 = create_lattice(prism_5, pf_z[4], 'prism_cell_5', 15)
prism_cell_6 = create_lattice(prism_6, pf_z[5], 'prism_cell_6', 16)
prism_cell_7 = create_lattice(prism_7, pf_z[6], 'prism_cell_7', 17)
prism_cell_8 = create_lattice(prism_8, pf_z[7], 'prism_cell_8', 18)
prism_cell_9 = create_lattice(prism_9, pf_z[8], 'prism_cell_9', 19)
prism_cell_10 = create_lattice(prism_10, pf_z[9], 'prism_cell_10', 20)

univ = openmc.Universe(
    cells=[
        bounds, 
        graphite1,
        graphite2,
        prism_cell_1,
        prism_cell_2,
        prism_cell_3,
        prism_cell_4,
        prism_cell_5,
        prism_cell_6,
        prism_cell_7,
        prism_cell_8,
        prism_cell_9,
        prism_cell_10,
    ]
)
geom = openmc.Geometry(univ)

# settings
point = openmc.stats.Point((13.5, 1.7, T_pitch*9.5))
src = openmc.Source(space=point)
settings = openmc.Settings()
settings.source = src
settings.batches = 80
settings.inactive = 20
settings.particles = 8000
settings.temperature = {"multipole": True, "method": "interpolation"}

plot = openmc.Plot()
plot.basis = "xy"
plot.origin = (13.5, 1.7, T_pitch*9.5)
plot.width = (30, 4)
plot.pixels = (1000, 200)
colors = {
    uoc_9: "black",
    graphite: "grey",
    flibe: "blue",  
    lm_graphite: "red",
    triso_4_layers: "black"
}
plot.color_by = "material"
plot.colors = colors
plots = openmc.Plots()
plots.append(plot)
"""
# MGXS 
# option 2 cole gentry 
groups = openmc.mgxs.EnergyGroups([1e-6, 1.8554, 2.9023e1, 9.1188e3, 2.0e7])
mgxs_lib = openmc.mgxs.Library(geom)
mgxs_lib.energy_groups = groups
mgxs_lib.domain_type = "cell"
mgxs_lib.domains = [
        bounds, 
        graphite1,
        graphite2,
        prism_cell_1,
        prism_cell_2,
        prism_cell_3,
        prism_cell_4,
        prism_cell_5,
        prism_cell_6,
        prism_cell_7,
        prism_cell_8,
        prism_cell_9,
        prism_cell_10,
    ]
mgxs_lib.by_nuclide = False
mgxs_lib.mgxs_types = ['total', 'absorption', 'nu-fission', 'fission',
                       'nu-scatter matrix', 'multiplicity matrix', 'chi']
mgxs_lib.legendre_order = 3
mgxs_lib.check_library_for_openmc_mgxs()
mgxs_lib.build_library()

# tallies 
tallies_file = openmc.Tallies()
mgxs_lib.add_to_tallies_file(tallies_file, merge=True)
mesh = openmc.RegularMesh()
mesh.dimension = [26, 1, 1]
mesh.lower_left = [0, 0, 0]
mesh.upper_right = [25.2,  0.4,  2.2]
mesh_filter = openmc.MeshFilter(mesh)
tally = openmc.Tally(name='mesh tally')
tally.filters = [mesh_filter]
tally.scores = ['fission']
tallies_file.append(tally, merge=True)"""

"""
# Moltres group constants 
# tallies 
all_cells = [
        bounds, 
        graphite1,
        graphite2,
        prism_cell_1,
        prism_cell_2,
        prism_cell_3,
        prism_cell_4,
        prism_cell_5,
        prism_cell_6,
        prism_cell_7,
        prism_cell_8,
        prism_cell_9,
        prism_cell_10,
    ]
all_cells_id = []
for c in all_cells:
    all_cells_id.append(c.id)
tallies_file = openmc.Tallies()
domain_dict = openmc_xs.generate_openmc_tallies_xml(
    [1e-6, 1.8554, 2.9023e1, 9.1188e3, 2.0e7],
    list(range(1, 7)),
    all_cells,
    all_cells_id,
    tallies_file,
)"""

# Comparison key neutronics parameters 
tallies_file = openmc.Tallies()
# beta
beta_mesh = openmc.RegularMesh()
beta_mesh.dimension = [1, 1, 1]
beta_mesh.lower_left = [0, 0, 0]
beta_mesh.upper_right = [27.1,  3.25,  1.85]
beta_mesh_filter = openmc.MeshFilter(beta_mesh)
beta_tally = openmc.Tally(name='beta')
beta_tally.filters = [beta_mesh_filter]
beta_tally.scores = ['delayed-nu-fission', 'nu-fission']
tallies_file.append(beta_tally, merge=True)

# flux 
energy_filter = openmc.EnergyFilter([1e-6, 1.8554, 2.9023e1, 9.1188e3, 2.0e7])
mesh_flux = openmc.RegularMesh()
mesh_flux.dimension = [100, 20, 1]
mesh_flux.lower_left = [0, 0, 0]
mesh_flux.upper_right = [27.1,  3.25,  1.85]
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
mesh_spectrum.dimension = [1, 1, 1]
mesh_spectrum.lower_left = [0, 0, 0]
mesh_spectrum.upper_right = [27.1,  3.25,  1.85]
mesh_filter_spectrum = openmc.MeshFilter(mesh_spectrum)
tally_spectrum_all = openmc.Tally(name='spectrum all')
tally_spectrum_all.filters = [mesh_filter_spectrum, energy_filter_all]
tally_spectrum_all.scores = ['flux', 'nu-fission', 'fission']
tallies_file.append(tally_spectrum_all)

tally_spectrum_4 = openmc.Tally(name='spectrum 4 groups')
tally_spectrum_4.filters = [mesh_filter_spectrum, energy_filter]
tally_spectrum_4.scores = ['flux', 'nu-fission', 'fission']
tallies_file.append(tally_spectrum_4)

# export 
mats.export_to_xml()
geom.export_to_xml()
settings.export_to_xml()
plots.export_to_xml()
tallies_file.export_to_xml()
#openmc.run(openmc_exec="openmc-ccm-nompi",threads=32)
