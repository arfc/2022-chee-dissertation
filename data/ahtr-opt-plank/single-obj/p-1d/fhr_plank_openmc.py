import openmc
import numpy as np
from numpy import sin
import sys 
sys.path.insert(1, '../../../../scripts/')
from plank_constants import *
from channel_variations_correct import * 

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
radius_bot = {{radius_bot}}
radius_top = {{radius_top}}
total_pf = {{total_pf}}

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
prism_cells = add_fuel_cells(total_pf, 0, 0, 0, constant=True)

# XML 
all_cells = [graphite1, graphite2, 
             flibe_bot, flibe_top, 
             graphite_filler_bot, graphite_filler_top]
for i in range(10):
    all_cells.append(prism_cells[i])
universe = openmc.Universe(cells=all_cells)
geom = openmc.Geometry(universe)


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

#openmc.run()