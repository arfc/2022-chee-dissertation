import numpy as np
import sys 
sys.path.insert(1, '../../../../scripts/')
from assem_coolant_mesh_generation import *

r1 = {{r1}}
r2 = {{r2}}
r3 = {{r3}}
r4 = {{r4}}
r5 = {{r5}}

radius_vals = [r1, r2, r3, r4, r5]

coolant_variation_points_curves_oup, new_line1, up, down, extra_line = coolant_variation_points_curves(radius_vals)
generate_inner_flibe_lines_surfaces_oup, new_line2 = generate_inner_flibe_lines_surfaces(new_line1, up, down, extra_line)
generate_plank_lines_surfaces_oup, new_line3 = generate_plank_lines_surfaces(new_line2, up, down, extra_line, new_line1)
generated_geo = generate_outer_flibe() + \
                generate_slot_flibe() + \
                generate_fuel_cells() + \
                generate_plank_points() + \
                generate_inner_flibe_points() + \
                coolant_variation_points_curves_oup + \
                generate_inner_flibe_lines_surfaces_oup + \
                generate_plank_lines_surfaces_oup + \
                graphite_structure_lines_surfaces(new_line3, new_line1, new_line2)

with open("fhr_assem_coolant_var.geo", "w") as geo_file:
    geo_file.write(generated_geo)