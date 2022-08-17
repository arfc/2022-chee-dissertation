import sys
sys.path.insert(1, '../../../')
from assem_constants import *  # noqa

# Templated Inputs
sine_a_x, sine_b_x, sine_c_x = 1.1308915254033483, 0.3817233110582547, 2.396688132402171
sine_a_y, sine_b_y, sine_c_y = 1.4305967007110234, 1.4874198268967571, 5.853070501261578
total_pf = 0.06

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

# flux 
energy_filter = openmc.EnergyFilter([1e-6, 1.8554, 2.9023e1, 9.1188e3, 2.0e7])
mesh_flux = openmc.RegularMesh()
mesh_flux.dimension = [100, 100]
mesh_flux.lower_left = [0, 0]
mesh_flux.upper_right = [pc.H_side_big+H_half_point_adj, H_half_point]
mesh_filter_flux = openmc.MeshFilter(mesh_flux)
tally_flux = openmc.Tally(name='flux')
tally_flux.filters = [mesh_filter_flux, energy_filter]
tally_flux.scores = [
    'flux',
    'nu-fission',
    'fission',]
tallies_file.append(tally_flux)

mats.export_to_xml()
geom.export_to_xml()
plots.export_to_xml()
settings.export_to_xml()
tallies_file.export_to_xml()