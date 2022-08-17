import openmc
import numpy as np
from numpy import sin
import sys 
sys.path.insert(1, '../../../ahtr_multiphysics/')
from constants import *
sys.path.insert(1, '../../../coolant_channel_shape/auto-mesh-moltres/')
from channel_variations_correct import * 
sys.path.insert(1, '../../../../moltres/python')
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
total_pf = 0.03575874580945256
sine_a = 0.002863419608893414
sine_b = 0.5231501671980268
sine_c = 3.818030550595
radius_bot = 0.24463990017087708
radius_top = 0.06238755285238676

# graphite left 
graphite1 = openmc.Cell(fill=graphite, cell_id=20001)
graphite1.region = +x_left & -plank_x_left & -y_top & +y_bot & -z_top & +z_bot
# graphite right
graphite2 = openmc.Cell(fill=graphite, cell_id=20002)
graphite2.region = +plank_x_right & -x_right & -y_top & +y_bot & -z_top & +z_bot
# flibe bottom 
flibe_bot = openmc.Cell(fill=flibe, cell_id=20003)
flibe_bot.region = +y_bot & -flibe_bot_top & +plank_x_left & -plank_x_right & -z_top & +z_bot

# flibe top 
flibe_top = openmc.Cell(fill=flibe, cell_id=20004)
flibe_top.region = +flibe_top_bot & -y_top & +plank_x_left & -plank_x_right & -z_top & +z_bot

# create channel variation
flibe_bot.region = remove_inward_flibe(True, radius_bot, flibe_bot.region)
flibe_top.region = remove_inward_flibe(False, radius_top, flibe_top.region)
flibe_bot.region = add_outward_flibe(True, radius_bot, flibe_bot.region)
flibe_top.region = add_outward_flibe(False, radius_top, flibe_top.region)
graphite_filler_bot, graphite_filler_top = add_graphite_fillers(flibe_bot.region, flibe_top.region)

# create fuel cells 
prism_cells = add_fuel_cells(total_pf, sine_a, sine_b, sine_c, constant=False)

# XML 
all_cells = [graphite1, graphite2, 
             flibe_bot, flibe_top, 
             graphite_filler_bot, graphite_filler_top]
for i in range(10):
    all_cells.append(prism_cells[i])
universe = openmc.Universe(cells=all_cells)
geom = openmc.Geometry(universe)

# tallies 
tallies_file = openmc.Tallies()
# ppf tallies 
energy_filter = openmc.EnergyFilter([1e-8, 20.0e7])
mesh = openmc.RegularMesh(mesh_id=1)
mesh.dimension = [10, 5]
mesh.lower_left = [2, 0.70]
mesh.upper_right = [25.1, 2.55]
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

# plot 
plot = openmc.Plot()
plot.basis = "xy"
plot.origin = (13, 1.5, T_pitch*10)
plot.width = (32, 4)
plot.pixels = (1600, 200)
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

# settings
point = openmc.stats.Point((13.5, 1.7, T_pitch*9.5))
src = openmc.Source(space=point)
settings = openmc.Settings()
settings.source = src
settings.batches = 80
settings.inactive = 20
settings.particles = 8000
settings.temperature = {"multipole": True, "method": "interpolation"}

# XML 
mats.export_to_xml()
geom.export_to_xml()
plots.export_to_xml()
settings.export_to_xml()
tallies_file.export_to_xml()

#openmc.run()
