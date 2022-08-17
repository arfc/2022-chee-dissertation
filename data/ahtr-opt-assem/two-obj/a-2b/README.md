# AHTR One-Third Assembly Optimization, Simulation a-2b

The results are presented in Section 7.3.2 of the dissertation. 

This optimization simulation was run on the Theta supercomputer using the `run.sh` bash script. 
The CLI output from Theta is printed in `599096.output`. 

The `run.sh` bash script uses ROLLO to run the following input file `rollo_a_2b.json`, which also uses the following evaluator scripts:  `fhr_assem_openmc.py` and `fhr_assem_openmc_output.py`.

The ROLLO output file is `checkpoint.pkl` and is analyzed using `assem_two_obj_2b.ipynb`.

All the `*.png` figures in this directory are included in the dissertation.  

`a-2b-comparison.ipynb` conducts a comparison study used in Section 7.3.4 of the dissertation. It uses files from `/most_minimized_both_gen5_corrected/`, `/most_minimized_pf_gen5_corrected/`, and `/most_minimized_ppf_gen5_corrected/`. 