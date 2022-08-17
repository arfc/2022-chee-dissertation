import sys
sys.path.insert(1, "../../../scripts/")
from assem_constants_coolant_channel_var import *
sys.path.insert(1, '../../../../../moltres/python')
from moltres_xs import *  # noqa: E402

total_pf = 0.04
r1 = 0.3362126603498319
r2 = 0.19332900646200954
r3 = 0.22466264505245426
r4 = 0.2171124986123351
r5 = 0.32187755642796423

pf_distr = np.array([[total_pf] * 10] * 6)

radius_vals = [r1, r2, r3, r4, r5]
P_cells, D_cell = remove_inward_flibe(radius_vals, P_cells, D_cell)
P_cells, D_cell = add_outer_graphite(radius_vals, P_cells, D_cell)

F_cells = create_fuel_cells(pf_distr)
all_cells = [
    H_cell,
    Hi_cell,
    D_cell,
    CS_cell] + P_cells + F_cells

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

universe = openmc.Universe(cells=all_cells)
geom = openmc.Geometry(universe)
settings.batches = 80
settings.inactive = 20
settings.particles = 8000

mats.export_to_xml()
geom.export_to_xml()
plots.export_to_xml()
settings.export_to_xml()
tallies_file.export_to_xml()  