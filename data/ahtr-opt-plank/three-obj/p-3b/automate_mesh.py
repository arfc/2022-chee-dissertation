import numpy as np
import sys 
sys.path.insert(1, '../../../coolant_channel_shape/auto-mesh-moltres/')
from automate_mesh_fns import *

radius_bot = {{radius_bot}}
radius_top = {{radius_top}}

graphite = graphite_geo()
fuelcells = fuelcells_geo()
coolant_bot, end_pt, end_line, end_surface = coolant_geo(bottom=True, radius=radius_bot, start_pt=34, start_line=46, start_surface=12)
coolant_top, end_pt, end_line, end_surface = coolant_geo(bottom=False, radius=radius_top, start_pt=end_pt, start_line=end_line, start_surface=end_surface)
geo_file_lines = graphite + fuelcells + coolant_bot + coolant_top
with open("fhr_plank.geo", "w") as geo_file:
    geo_file.write(geo_file_lines)