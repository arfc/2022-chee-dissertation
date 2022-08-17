import sys
sys.path.insert(1, '../../../../scripts/')
from assem_constants import *  # noqa
sys.path.insert(1, '../../../../../../moltres/python')
from moltres_xs import *  # noqa: E402

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
all_cells = [
    H_cell,
    Hi_cell,
    D_cell,
    CS_cell] + P_cells + F_cells
universe = openmc.Universe(
    cells=all_cells)

geom = openmc.Geometry(universe)
settings.batches = 80
settings.inactive = 20
settings.particles = 8000

# tallies 
tallies_file = openmc.Tallies()
# Moltres group constants 
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

mats.export_to_xml()
geom.export_to_xml()
plots.export_to_xml()
settings.export_to_xml()
tallies_file.export_to_xml()