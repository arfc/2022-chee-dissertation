# AHTR Plank Optimization, Simulation p-2a

The results are presented in Section 6.3.1 of the dissertation. 

This optimization simulation was run on the Theta supercomputer using the `run.sh` bash script. 
The CLI output from Theta is printed in `585314.output`. 

The `run.sh` bash script uses ROLLO to run the following input file `rollo_two_obj_pf_ppf.json`, which also utilizes the following evaluator scripts:  `fhr_plank_openmc.py` and `fhr_plank_openmc_output.py`.

The ROLLO output file is `checkpoint_update.pkl` and is analyzed using `pf_ppf_analysis_update.ipynb`. 

The `most_minimized_pf` directory contains the AHTR plank model with the most-minimized 
PF. The `most_minimized_ppf` directory contains the AHTR plank model with the
most-minimized PPF. 

`new_0.029_flux_comparison.ipynb` conducts a flux comparison study used in Section 6.3.4 of the dissertation. It uses files from `/most_minimized_ppf/` and `/p1c_shape/`. 

All the `*.png` figures in this directory are included in the dissertation.  
