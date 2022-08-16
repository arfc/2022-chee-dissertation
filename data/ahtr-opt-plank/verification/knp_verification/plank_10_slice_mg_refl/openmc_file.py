import openmc
import numpy as np

T_pitch = 0.09266

# materials
flibe_mg = openmc.Material(name="flibe", material_id=1)
flibe_mg.add_macroscopic("bounds")
graphite1_mg = openmc.Material(name="graphite1", material_id=2)
graphite1_mg.add_macroscopic("graphite1")
graphite2_mg = openmc.Material(name="graphite2", material_id=3)
graphite2_mg.add_macroscopic("graphite2")
prism_cell_1_mg = openmc.Material(name="prism_cell_1", material_id=4)
prism_cell_1_mg.add_macroscopic("prism_cell_1")
prism_cell_2_mg = openmc.Material(name="prism_cell_2", material_id=5)
prism_cell_2_mg.add_macroscopic("prism_cell_2")
prism_cell_3_mg = openmc.Material(name="prism_cell_3", material_id=6)
prism_cell_3_mg.add_macroscopic("prism_cell_3")
prism_cell_4_mg = openmc.Material(name="prism_cell_4", material_id=7)
prism_cell_4_mg.add_macroscopic("prism_cell_4")
prism_cell_5_mg = openmc.Material(name="prism_cell_5", material_id=8)
prism_cell_5_mg.add_macroscopic("prism_cell_5")
prism_cell_6_mg = openmc.Material(name="prism_cell_6", material_id=9)
prism_cell_6_mg.add_macroscopic("prism_cell_6")
prism_cell_7_mg = openmc.Material(name="prism_cell_7", material_id=10)
prism_cell_7_mg.add_macroscopic("prism_cell_7")
prism_cell_8_mg = openmc.Material(name="prism_cell_8", material_id=11)
prism_cell_8_mg.add_macroscopic("prism_cell_8")
prism_cell_9_mg = openmc.Material(name="prism_cell_9", material_id=12)
prism_cell_9_mg.add_macroscopic("prism_cell_9")
prism_cell_10_mg = openmc.Material(name="prism_cell_10", material_id=13)
prism_cell_10_mg.add_macroscopic("prism_cell_10")

mats = openmc.Materials(
    (
        flibe_mg,
        graphite1_mg,
        graphite2_mg,
        prism_cell_1_mg,
        prism_cell_2_mg,
        prism_cell_3_mg,
        prism_cell_4_mg,
        prism_cell_5_mg,
        prism_cell_6_mg,
        prism_cell_7_mg,
        prism_cell_8_mg,
        prism_cell_9_mg,
        prism_cell_10_mg,
    )
)
mats.cross_sections = "../plank_10_slice_refl/mgxs.h5"

bounds = openmc.Cell(fill=flibe_mg)
x_left = +openmc.XPlane(x0=0, boundary_type="reflective")
x_right = -openmc.XPlane(x0=27.1, boundary_type="reflective")
y_top = -openmc.YPlane(y0=3.25, boundary_type="reflective")
y_bot = +openmc.YPlane(y0=0, boundary_type="reflective")
z_top = -openmc.ZPlane(z0=T_pitch * 20, boundary_type="reflective")
z_bot = +openmc.ZPlane(z0=0, boundary_type="reflective")
bounds.region = x_left & x_right & y_top & y_bot & z_top & z_bot

plank_x_left = +openmc.XPlane(x0=2)
plank_x_right = -openmc.XPlane(x0=2 + 23.1)
plank_y_top = -openmc.YPlane(y0=0.35 + 2.55)
plank_y_bot = +openmc.YPlane(y0=0.35)
plank_region = plank_x_left & plank_x_right & plank_y_top & plank_y_bot & z_top & z_bot
bounds.region &= ~plank_region

graphite1_x_right = -openmc.XPlane(x0=2)
graphite1 = openmc.Cell(fill=graphite1_mg)
graphite1.region = x_left & graphite1_x_right & y_top & y_bot & z_top & z_bot
bounds.region &= ~graphite1.region

graphite2_x_left = +openmc.XPlane(x0=25.1)
graphite2 = openmc.Cell(fill=graphite2_mg)
graphite2.region = graphite2_x_left & x_right & y_top & y_bot & z_top & z_bot
bounds.region &= ~graphite2.region

boundaries = np.arange(2, 27.1, 2.31)
prism_y_bot = +openmc.YPlane(y0=0.35)
prism_y_top = -openmc.YPlane(y0=0.35 + 2.55)
prism_z_bot = +openmc.ZPlane(z0=0, boundary_type="reflective")
prism_z_top = -openmc.ZPlane(z0=T_pitch * 20, boundary_type="reflective")
prism_1 = openmc.Cell(fill=prism_cell_1_mg)
prism_1.region = (
    +openmc.XPlane(x0=boundaries[0])
    & -openmc.XPlane(x0=boundaries[1])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_1.region
prism_2 = openmc.Cell(fill=prism_cell_2_mg)
prism_2.region = (
    +openmc.XPlane(x0=boundaries[1])
    & -openmc.XPlane(x0=boundaries[2])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_2.region
prism_3 = openmc.Cell(fill=prism_cell_3_mg)
prism_3.region = (
    +openmc.XPlane(x0=boundaries[2])
    & -openmc.XPlane(x0=boundaries[3])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_3.region
prism_4 = openmc.Cell(fill=prism_cell_4_mg)
prism_4.region = (
    +openmc.XPlane(x0=boundaries[3])
    & -openmc.XPlane(x0=boundaries[4])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_4.region
prism_5 = openmc.Cell(fill=prism_cell_5_mg)
prism_5.region = (
    +openmc.XPlane(x0=boundaries[4])
    & -openmc.XPlane(x0=boundaries[5])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_5.region
prism_6 = openmc.Cell(fill=prism_cell_6_mg)
prism_6.region = (
    +openmc.XPlane(x0=boundaries[5])
    & -openmc.XPlane(x0=boundaries[6])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_6.region
prism_7 = openmc.Cell(fill=prism_cell_7_mg)
prism_7.region = (
    +openmc.XPlane(x0=boundaries[6])
    & -openmc.XPlane(x0=boundaries[7])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_7.region
prism_8 = openmc.Cell(fill=prism_cell_8_mg)
prism_8.region = (
    +openmc.XPlane(x0=boundaries[7])
    & -openmc.XPlane(x0=boundaries[8])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_8.region
prism_9 = openmc.Cell(fill=prism_cell_9_mg)
prism_9.region = (
    +openmc.XPlane(x0=boundaries[8])
    & -openmc.XPlane(x0=boundaries[9])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_9.region
prism_10 = openmc.Cell(fill=prism_cell_10_mg)
prism_10.region = (
    +openmc.XPlane(x0=boundaries[9])
    & -openmc.XPlane(x0=boundaries[10])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_10.region

univ = openmc.Universe(
    cells=[
        bounds,
        graphite1,
        graphite2,
        prism_1,
        prism_2,
        prism_3,
        prism_4,
        prism_5,
        prism_6,
        prism_7,
        prism_8,
        prism_9,
        prism_10,
    ]
)
geom = openmc.Geometry(univ)

# settings
point = openmc.stats.Point((13.5, 1.7, T_pitch * 9.5))
src = openmc.Source(space=point)
settings = openmc.Settings()
settings.source = src
settings.batches = 80
settings.inactive = 20
settings.particles = 8000
settings.temperature = {"multipole": True, "method": "interpolation"}
settings.energy_mode = "multi-group"

plot = openmc.Plot()
plot.basis = "xy"
plot.origin = (13.5, 1.7, T_pitch * 9.5)
plot.width = (30, 4)
plot.pixels = (1000, 200)
colors = {
    flibe_mg: "blue",
    graphite1_mg: "grey",
    graphite2_mg: "red",
    prism_cell_1_mg: "pink", 
    prism_cell_2_mg: "yellow", 
    prism_cell_3_mg: "orange", 
    prism_cell_4_mg: "green", 
    prism_cell_5_mg: "purple", 
    prism_cell_6_mg: "pink", 
    prism_cell_7_mg: "yellow", 
    prism_cell_8_mg: "orange", 
    prism_cell_9_mg: "green", 
    prism_cell_10_mg: "purple", 
}
plot.color_by = "material"
plot.colors = colors
plots = openmc.Plots()
plots.append(plot)

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
#openmc.run(openmc_exec="openmc-ccm-nompi", threads=32)
