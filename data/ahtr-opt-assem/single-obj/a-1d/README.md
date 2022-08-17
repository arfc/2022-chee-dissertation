# AHTR Plank Optimization, Simulation a-1d

The results are presented in Section 7.2.1 of the dissertation. 

This optimization simulation was run on the Theta supercomputer using the `run.sh` bash script. 
The CLI output from Theta is printed in `601664.output`. 

The `run.sh` bash script uses ROLLO to run the following input file `rollo_assem_min_pf.json`, which also utilizes the following evaluator scripts:  `fhr_assem_openmc.py` and `fhr_assem_openmc_keff.py`.

The ROLLO output file is `checkpoint.pkl` and is analyzed using `assem_coolant_pf_one_obj.ipynb`.

All the `*.png` figures in this directory are included in the dissertation.  
