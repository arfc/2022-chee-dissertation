import sys 
sys.path.insert(1, "../../../coolant_variation/")
from assem_constants_coolant_channel_var import *
sys.path.insert(1, '../../../../../moltres/python')
from moltres_xs import *  # noqa: E402

# Templated Inputs
sine_a_x, sine_b_x, sine_c_x = 1.2015933482640977, 1.317782916915506, 3.6650990316392997
sine_a_y, sine_b_y, sine_c_y = 1.7202238067665359, 1.3075280916075396, 4.122926290592964
total_pf = 0.053756148172940214
r1 = 0.21889787411014983
r2 = 0.1103255214427411
r3 = 0.2890944605903698
r4 = 0.28533884833531487
r5 = 0.30899892853872923

pf_distr = triso_distr(
    total_pf,
    sine_a_x,
    sine_b_x,
    sine_c_x,
    sine_a_y,
    sine_b_y,
    sine_c_y)

radius_vals = [r1, r2, r3, r4, r5]
P_cells, D_cell = remove_inward_flibe(radius_vals, P_cells, D_cell)
P_cells, D_cell = add_outer_graphite(radius_vals, P_cells, D_cell)

F_cells = create_fuel_cells(pf_distr)
all_cells = [
    H_cell,
    Hi_cell,
    D_cell,
    CS_cell] + P_cells + F_cells

universe = openmc.Universe(cells=all_cells)
geom = openmc.Geometry(universe)
settings.batches = 80
settings.inactive = 20
settings.particles = 8000

# tallies 
tallies_file = openmc.Tallies()

# PPF 
energy_filter = openmc.EnergyFilter([1e-8, 20.0e7])
for j in range(6):
    y_lower_left = first_fuel_cell_bot - j * ygap_btwn_fuel_cells
    F_i_starting_point = F_starting_point + j * xgap_btwn_fuel_cells
    mesh = openmc.RegularMesh(mesh_id=j+1)
    mesh.dimension = [10, 5]
    mesh.lower_left = [F_i_starting_point, y_lower_left]
    mesh.upper_right = [F_i_starting_point+10*F_cell_width, y_lower_left+F_cell_height]
    mesh_filter = openmc.MeshFilter(mesh)
    fqr_tally = openmc.Tally(name='fqr_'+str(j+1))
    fqr_tally.filters = [energy_filter, mesh_filter]
    fqr_tally.scores = ['fission-q-recoverable', 'nu-fission', 'fission']
    tallies_file.append(fqr_tally)

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