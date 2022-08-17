import openmc
import numpy as np
import fhr_assem_openmc as input_file

h5file = "statepoint.80.h5"
sp = openmc.StatePoint(h5file, autolink=False)
keff = sp.k_combined.nominal_value

def get_fuel_normalized_fqro(mesh_tally_name, pf_index):
    mesh_tally = sp.get_tally(name=mesh_tally_name)
    fqro = mesh_tally.get_slice(scores=['fission-q-recoverable'])
    fqro_list = fqro.mean
    fqro_list.shape = (5,10)
    fqro_array = np.array(fqro_list)
    normalized_array = fqro_array / input_file.pf_distr[pf_index]
    return normalized_array

huge_array = []
for i in range(1, 6):
    huge_array.append(get_fuel_normalized_fqro("fqr_"+str(i), i-1))

ppf = np.max(huge_array) / np.mean(huge_array)

print({"ppf": ppf, "keff": keff})
