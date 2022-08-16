# AHTR Plank Optimization, Simulation p-1f

The results are presented in Section 6.2.3 of the dissertation. 

This optimization simulation was run on the Theta supercomputer using the `run.sh` bash script. 
The CLI output from Theta is printed in `586475.output`. 

The `run.sh` bash script uses ROLLO to run the following input file `rollo_coolant_ppf.json`, which also utilizes the following evaluator scripts:  `fhr_plank_openmc.py` and `fhr_plank_openmc_output.py`.

The ROLLO output file is `checkpoint.pkl` and is analyzed using `coolant_one_obj_ppf.ipynb`. 

All the `*.png` figures in this directory are included in the dissertation.  