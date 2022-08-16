import openmc
h5file = "statepoint.80.h5"
sp = openmc.StatePoint(h5file, autolink=False)
keff = sp.k_combined.nominal_value

print({"keff2": keff})