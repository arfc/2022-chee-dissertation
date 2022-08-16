# AHTR Plank Optimization, Simulation p-1b

The results are presented in Section 6.2.2 of the dissertation. 

This optimization simulation was run on the Bluewaters supercomputer using the `run.o13267004` bash script. 
The CLI output from Bluewaters is printed in `run.o13562143`. 

The `run` bash script uses ROLLO to run the following input file `rollo_min_temp.json`, which also utilizes the following evaluator scripts:  `fhr_plank_openmc.py`, `fhr_plank_openmc_keff.py`, `fhr_plank_moltres.i`, `fhr_plank.msh`, `fhr_plank_gc.inp`, `summary_dummy.h5`, and `fhr_plank_moltres_output.py`.

The ROLLO output file is `checkpoint.pkl` and is analyzed using `rollo_min_temp_analysis.ipynb`.

All the `*.png` figures in this directory are included in the dissertation.  
