# AHTR Plank Optimization, Simulation p-3b

The results are presented in Section 6.4.2 of the dissertation. 

This optimization simulation was run on the Theta supercomputer using the `run.sh` bash script. 
The CLI output from Theta is printed in `597001.output`. 

The `run.sh` bash script uses ROLLO to run the following input file `rollo_three_obj_all_param.json`, which also utilizes the following evaluator scripts:  `fhr_plank_openmc.py`, `fhr_plank_openmc_output.py`, `fhr_plank_gc.inp`, `fhr_plank_moltres.i`, `fhr_plank_moltres_output.py`, `fhr_plank.geo`, `fhr_plank.msh`, and `summary_dummy.h5`.

The ROLLO output file is `checkpoint.pkl` and is analyzed using `all_param_pf_temp_ppf_three_obj_analysis.ipynb`. 

The `5_33` directory contains the AHTR plank model with the most-minimized 
PF. The `3_11` directory contains the AHTR plank model with the most-minimized max temp. The `6_123` directory contains the AHTR plank model with the most-minimized PPF. 

All the `*.png` figures in this directory are included in the dissertation.  
