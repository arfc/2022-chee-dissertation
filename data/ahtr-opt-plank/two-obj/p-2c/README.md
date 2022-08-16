# AHTR Plank Optimization, Simulation p-2c

The results are presented in Section 6.3.3 of the dissertation. 

This optimization simulation was run on the Theta supercomputer using the `run.sh` bash script. 
The CLI output from Theta is printed in `584901.output`. 

The `run.sh` bash script uses ROLLO to run the following input file `rollo_two_obj_temp_ppf.json`, which also utilizes the following evaluator scripts:  `fhr_plank_openmc.py`, `fhr_plank_openmc_output.py`, `fhr_plank_gc.inp`, `fhr_plank_moltres.i`, 
`fhr_plank_moltres_output.py`, `fhr_plank.geo`, `fhr_plank.msh`, and `summary_dummy.h5`.

The ROLLO output file is `checkpoint.pkl` and is analyzed using `temp_ppf_analysis1.ipynb`. 

The `most_minimized_temp` directory contains the AHTR plank model with the most-minimized max temp. The `most_minimized_ppf` directory contains the AHTR plank model with the most-minimized PPF. 

All the `*.png` figures in this directory are included in the dissertation.  
