# AHTR Plank Optimization, Simulation a-1c

The results are presented in Section 7.2.3 of the dissertation. 

This optimization simulation was run on the Theta supercomputer using the `run.sh` bash script. 
The CLI output from Theta is printed in `604489.output`. 

The `run.sh` bash script uses ROLLO to run the following input file `rollo_assem_min_ppf.json`, which also utilizes the following evaluator scripts:  `fhr_assem_openmc.py` and `fhr_assem_openmc_output.py`.

The ROLLO output file is `checkpoint.pkl` and is analyzed using `assem_one_obj_ppf.ipynb`.

All the `*.png` figures in this directory are included in the dissertation.  

`a-1c-comparison.ipynb` conducts a comparison study used in Section 7.2.4 of the dissertation. It uses files from `/flat_distr_gen0_64/`, `/least_minimized_gen1_128/`, and `/most_minimized_gen0_64/`. 