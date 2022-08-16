import openmc
import sys 
sys.path.insert(1, '../')
from benchmark_openmc import *

sp = openmc.StatePoint("./openmc_mgxs/mg_statepoint.80.h5", autolink=False)
su = openmc.Summary("./openmc_mgxs/mg_summary.h5")
sp.link_with_summary(su)
mgxs_lib.load_from_statepoint(sp)

mgxs_file = mgxs_lib.create_mg_library(
    xs_type="macro",
    xsdata_names=[
        "outer_flibe",
        "graphite_structure",
        "spacers",
        "slot_flibe",
        "inner_flibe_1", 
        "inner_flibe_2", 
        "inner_flibe_3", 
        "P_1_1",
        "P_1_2",
        "P_1_3",
        "P_1_4",
        "P_1_5",
        "P_1_6",
        "P_2_1",
        "P_2_2",
        "P_2_3",
        "P_2_4",
        "P_2_5",
        "P_2_6",
        "P_3_1",
        "P_3_2",
        "P_3_3",
        "P_3_4",
        "P_3_5",
        "P_3_6",
        "fuel_1_1",
        "fuel_1_2",
        "fuel_1_3",
        "fuel_1_4",
        "fuel_1_5",
        "fuel_1_6",
        "fuel_1_7",
        "fuel_1_8",
        "fuel_1_9",
        "fuel_1_10",
        "fuel_1_11",
        "fuel_1_12",
        "fuel_2_1",
        "fuel_2_2",
        "fuel_2_3",
        "fuel_2_4",
        "fuel_2_5",
        "fuel_2_6",
        "fuel_2_7",
        "fuel_2_8",
        "fuel_2_9",
        "fuel_2_10",
        "fuel_2_11",
        "fuel_2_12",
        "fuel_3_1",
        "fuel_3_2",
        "fuel_3_3",
        "fuel_3_4",
        "fuel_3_5",
        "fuel_3_6",
        "fuel_3_7",
        "fuel_3_8",
        "fuel_3_9",
        "fuel_3_10",
        "fuel_3_11",
        "fuel_3_12",
    ]
)
mgxs_file.export_to_hdf5()
