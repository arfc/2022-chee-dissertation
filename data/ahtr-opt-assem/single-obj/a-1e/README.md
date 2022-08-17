# AHTR One-Third Assembly Optimization, Simulation a-1e

The results are presented in Section 7.2.2 of the dissertation. 

This optimization simulation was run on the Theta supercomputer using the `run.sh` bash script. 
The CLI output from Theta is printed in `606421.output`. 

The `run.sh` bash script uses ROLLO to run the following input file `rollo_assem_min_temp.json`, which also uses the following evaluator scripts:  `fhr_assem_openmc.py`, `fhr_assem_openmc_output.py`, `fhr_assem.geo`, 
`fhr_assem.msh`, `automate_mesh.py`, `mesh_generate.sh`, `fhr_assem_moltres.i`, `fhr_assem_moltres_output.py`, `fhr_assem_gc.inp`, and `summary_dummy.h5`.

The ROLLO output file is `checkpoint.pkl` and is analyzed using `assem_coolant_temp_one_obj.ipynb`.

All the `*.png` figures in this directory are included in the dissertation.  

`plot_temp.ipynb` plots the temperature distribution for the AHTR model that most-minimized Tmax. Its results are held in `/most_minimized_gen2_64/`.