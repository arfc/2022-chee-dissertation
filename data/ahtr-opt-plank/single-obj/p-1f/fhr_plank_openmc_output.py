import openmc
from fhr_plank_openmc import * 
h5file = "statepoint.80.h5"
sp = openmc.StatePoint(h5file, autolink=False)
summary = openmc.Summary("../summary_dummy.h5")
sp.link_with_summary(summary)

keff = sp.k_combined.nominal_value

mesh_tally = sp.get_tally(name='fqr')
fqro = mesh_tally.get_slice(scores=['fission-q-recoverable'])
nu_fission = mesh_tally.get_slice(scores=['nu-fission'])
fission = mesh_tally.get_slice(scores=['fission'])
fqro_list = fqro.mean
fqro_list.shape = (5,10)
fqro_array = np.array(fqro_list)
nu_fission_list = nu_fission.mean
nu_fission_list.shape = (5,10)
nu_fission_array = np.array(nu_fission_list)
fission_list = fission.mean
fission_list.shape = (5,10)
fission_array = np.array(fission_list)
ppf = np.max((fqro_array))/ np.mean(fqro_array)

print({"ppf": ppf, "keff2": keff})