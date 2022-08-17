import sys 
sys.path.insert(1, "../../../")
from assem_constants_coolant_channel_var import *

total_pf = 0.06
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

tallies_file = openmc.Tallies()
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

mats.export_to_xml()
geom.export_to_xml()
plots.export_to_xml()
settings.export_to_xml()
tallies_file.export_to_xml()
