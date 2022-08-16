# AHTR Plank Optimization, Simulation p-1c

The results are presented in Section 6.2.1 of the dissertation. 

This optimization simulation was run on the Theta supercomputer using the `run.sh` bash script. 
The CLI output from Theta is printed in `593934.output`. 

The `run` bash script uses ROLLO to run the following input file `rollo_coolant_pf.json`, which also utilizes the following evaluator scripts:  `fhr_plank_openmc.py` and `fhr_plank_openmc_output.py`.

The ROLLO output file is `checkpoint.pkl` and is analyzed using `coolant_one_obj_pf.ipynb`. 

All the `*.png` figures in this directory are included in the dissertation.  
