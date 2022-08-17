import sys 
sys.path.insert(1, '../../../../scripts/')
from assem_constants_coolant_channel_var import *
sys.path.insert(1, '../../../../../../moltres/python')
from moltres_xs import *  # noqa: E402

# Templated Inputs
sine_a_x, sine_b_x, sine_c_x = 0.07113071938360885, 0.39692017208047786, 3.2103493629626247
sine_a_y, sine_b_y, sine_c_y = 0.8249276238830685, 0.0743218031934757, 3.569827798143426
total_pf = 0.05601427680736762
r1 = 0.2321648189804043
r2 = 0.2021757476772288
r3 = 0.20427960719865618
r4 = 0.23354106149388104
r5 = 0.1450726700363517

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