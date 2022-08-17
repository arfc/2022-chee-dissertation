import sys
sys.path.insert(1, '../../../../scripts')
from assem_constants import *  # noqa

# Templated Inputs
sine_a_x, sine_b_x, sine_c_x = {{sine_a_x}}, {{sine_b_x}}, {{sine_c_x}}
sine_a_y, sine_b_y, sine_c_y = {{sine_a_y}}, {{sine_b_y}}, {{sine_c_y}}
total_pf = {{total_pf}}

pf_distr = triso_distr(
    total_pf,
    sine_a_x,
    sine_b_x,
    sine_c_x,
    sine_a_y,
    sine_b_y,
    sine_c_y)

F_cells = create_fuel_cells(pf_distr)

universe = openmc.Universe(
    cells=[
        H_cell,
        Hi_cell,
        D_cell,
        CS_cell] +
    P_cells +
    F_cells)

geom = openmc.Geometry(universe)
settings.batches = 80
settings.inactive = 20
settings.particles = 8000

mats.export_to_xml()
geom.export_to_xml()
plots.export_to_xml()
settings.export_to_xml()