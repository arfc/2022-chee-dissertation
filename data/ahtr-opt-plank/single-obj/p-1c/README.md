# AHTR Plank Optimization, Simulation p-1c

The results are presented in Section 6.2.3 of the dissertation. 

This optimization simulation was run on the Bluewaters supercomputer using the `run` bash script. 
The CLI output from Bluewaters is printed in `run.o13568566`. 

The `run` bash script uses ROLLO to run the following input file `rollo_min_ppf.json`, which also utilizes the following evaluator scripts:  `fhr_plank_openmc.py` and `fhr_plank_openmc_output.py`.

The ROLLO output file is `checkpoint.pkl` and is analyzed using `min_ppf_analysis.ipynb`.

All the `*.png` figures in this directory are included in the dissertation.  

`0.023_flux_comparison.ipynb` conducts a flux comparison study used in Section 6.2.4 of the dissertation. It uses files from `/most_minimized/` and `/flat_study/`. 