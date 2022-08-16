# AHTR Plank Optimization, Simulation p-2a

The results are presented in Section 6.3.1 of the dissertation. 

This optimization simulation was run on the Theta supercomputer using the `run.sh` bash script. 
The CLI output from Theta is printed in `585997.output`. 

The `run.sh` bash script uses ROLLO to run the following input file `rollo_two_obj.json`, which also utilizes the following evaluator scripts:  `fhr_plank_openmc.py`, `fhr_plank_openmc_keff.py`, `fhr_plank_gc.inp`, `fhr_plank_moltres.i`, 
`fhr_plank_moltres_output.py`, `fhr_plank.geo`, `fhr_plank.msh`, and `summary_dummy.h5`.

The ROLLO output file is `checkpoint.pkl` and is analyzed using `pf_temp_two_obj_analysis.ipynb`. 

The `openmc_gc_0_3` directory contains the AHTR plank model with the most-minimized 
PF. The `openmc_gc_0_84` directory contains the AHTR plank model with the
most-minimized max temp. 

All the `*.png` figures in this directory are included in the dissertation.  
