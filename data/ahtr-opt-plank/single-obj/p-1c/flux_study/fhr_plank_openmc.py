import openmc
import numpy as np
from numpy import sin, cos, tan, pi
import sys 
sys.path.insert(1, '../../../../scripts/')
from plank_constants import *
sys.path.insert(1, '../../../../../../moltres/python')
from moltres_xs import *  # noqa: E402

temp = 948
uoc_9.temperature = temp
por_c.temperature = temp
si_c.temperature = temp
graphite.temperature = temp
triso_4_layers.temperature = temp
lm_graphite.temperature = temp
flibe.temperature = temp
mats = openmc.Materials((uoc_9, por_c, si_c, graphite, lm_graphite, flibe, triso_4_layers))

# Templating
total_pf = 0.0979
sine_a = 0.7357603668525308
sine_b = 0.3603983534770009
sine_c = 6.078072711871279
vol_total = 23.1 * 2.55 * T_pitch * 20
vol_slice = 2.31 * 2.55 * T_pitch * 20

x_left = +openmc.XPlane(x0=0, boundary_type="reflective")
x_right = -openmc.XPlane(x0=27.1, boundary_type="reflective")
y_top = -openmc.YPlane(y0=3.25, boundary_type="reflective")
y_bot =  +openmc.YPlane(y0=0, boundary_type="reflective")
z_top = -openmc.ZPlane(z0=T_pitch*20, boundary_type="reflective")
z_bot = +openmc.ZPlane(z0=0, boundary_type="reflective")
bounds = openmc.Cell(fill=flibe, cell_id=4)
bounds.region = x_left & x_right & y_top & y_bot & z_top & z_bot

plank_x_left = +openmc.XPlane(x0=2)
plank_x_right = -openmc.XPlane(x0=2+23.1)
plank_y_top = -openmc.YPlane(y0=0.35+2.55)
plank_y_bot = +openmc.YPlane(y0=0.35)
plank_region = plank_x_left & plank_x_right & plank_y_top & plank_y_bot & z_top & z_bot
bounds.region &= ~plank_region

graphite1_x_right = -openmc.XPlane(x0=2)
graphite1 = openmc.Cell(fill=graphite, cell_id=5)
graphite1.region = x_left & graphite1_x_right & y_top & y_bot & z_top & z_bot
bounds.region &= ~graphite1.region

graphite2_x_left = +openmc.XPlane(x0=25.1)
graphite2 = openmc.Cell(fill=graphite, cell_id=6)
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

# tallies 
tallies_file = openmc.Tallies()

# ppf tallies 
energy_filter = openmc.EnergyFilter([1e-8, 20.0e7])
mesh = openmc.RegularMesh(mesh_id=1)
mesh.dimension = [10, 5]
mesh.lower_left = [2, 0.35]
mesh.upper_right = [25.1, 2.9]
mesh_filter = openmc.MeshFilter(mesh)
fqr_tally = openmc.Tally(name='fqr')
fqr_tally.filters = [energy_filter, mesh_filter]
fqr_tally.scores = ['fission-q-recoverable', 'nu-fission', 'fission']
tallies_file.append(fqr_tally, merge=True)

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

# flux all
energy_filter_all = openmc.EnergyFilter([1e-6, 2.0e7])
mesh_flux_all = openmc.RegularMesh()
mesh_flux_all.dimension = [100, 20, 1]
mesh_flux_all.lower_left = [0, 0, 0]
mesh_flux_all.upper_right = [27.1,  3.25,  1.85]
mesh_filter_flux_all = openmc.MeshFilter(mesh_flux_all)
tally_flux_all = openmc.Tally(name='flux_all')
tally_flux_all.filters = [mesh_filter_flux_all, energy_filter_all]
tally_flux_all.scores = [
    'flux',
    'nu-fission',
    'fission',]
tallies_file.append(tally_flux_all)

# export 
mats.export_to_xml()
geom.export_to_xml()
settings.export_to_xml()
plots.export_to_xml()
tallies_file.export_to_xml()
#openmc.run()
#print("here")
#openmc.run(openmc_exec="openmc-ccm-nompi",threads=16)