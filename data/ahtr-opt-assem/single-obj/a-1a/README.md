# AHTR Plank Optimization, Simulation p-1a

The results are presented in Section 7.2.1 of the dissertation. 

This optimization simulation was run on the Theta supercomputer using the `run.sh` bash script. 
The CLI output from Theta is printed in `604503.output`. 

The `run.sh` bash script uses ROLLO to run the following input file `rollo_assem_min_pf.json`, which also utilizes the following evaluator scripts:  `fhr_assem_openmc.py` and `fhr_assem_openmc_keff.py`.

The ROLLO output file is `checkpoint.pkl` and is analyzed using `assem_one_obj_pf.ipynb`.

All the `*.png` figures in this directory are included in the dissertation.  

`new-a-1a-comparison.ipynb` conducts a comparison study used in Section 6.2.4 of the dissertation. It uses files from `/most_minimized_gen1_128/` and `/flat_distr_gen1_128/`. 