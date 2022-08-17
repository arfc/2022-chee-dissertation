import sys 
sys.path.insert(1, "../../../../scripts/")
from assem_constants_coolant_channel_var import *

total_pf = {{total_pf}}
r1 = {{r1}}
r2 = {{r2}}
r3 = {{r3}}
r4 = {{r4}}
r5 = {{r5}}

pf_distr = np.array([[total_pf] * 10] * 6)

radius_vals = [r1, r2, r3, r4, r5]
P_cells, D_cell = remove_inward_flibe(radius_vals, P_cells, D_cell)
P_cells, D_cell = add_outer_graphite(radius_vals, P_cells, D_cell)

F_cells = create_fuel_cells(pf_distr)
universe = openmc.Universe(
    cells=[
    H_cell,
    Hi_cell,
    D_cell,
    CS_cell] + P_cells + F_cells)

geom = openmc.Geometry(universe)
settings.batches = 80
settings.inactive = 20
settings.particles = 8000

mats.export_to_xml()
geom.export_to_xml()
plots.export_to_xml()
settings.export_to_xml()