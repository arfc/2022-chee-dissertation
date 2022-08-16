import openmc
from openmc_file import *

sp = openmc.StatePoint("./140pcm/statepoint.80.h5", autolink=False)
su = openmc.Summary("./140pcm/summary.h5")
sp.link_with_summary(su)
mgxs_lib.load_from_statepoint(sp)

mgxs_file = mgxs_lib.create_mg_library(
    xs_type="macro",
    xsdata_names=[
        "bounds",
        "graphite1",
        "graphite2",
        "prism_cell_1",
        "prism_cell_2",
        "prism_cell_3",
        "prism_cell_4",
        "prism_cell_5",
        "prism_cell_6",
        "prism_cell_7",
        "prism_cell_8",
        "prism_cell_9",
        "prism_cell_10",
    ],
)
mgxs_file.export_to_hdf5()
