# AHTR Plank Optimization, Simulation p-1e

The results are presented in Section 6.2.2 of the dissertation. 

This optimization simulation was run on the Theta supercomputer using the `run.sh` bash script. 
The CLI output from Theta is printed in `593861.output`. 

The `run` bash script uses ROLLO to run the following input file `rollo_coolant_temp.json`, which also utilizes the following evaluator scripts:  `fhr_plank_openmc.py`, `fhr_plank_openmc_output.py`, `summary_dummy.h5`, `mesh_generate.sh`, `fhr_plank_moltres.i`, `fhr_plank_moltres_output.py`, `fhr_plank_gc.inp`, and 
`automate_mesh.py`.

The ROLLO output file is `checkpoint.pkl` and is analyzed using `coolant_one_obj_temp.ipynb`. 

All the `*.png` figures in this directory are included in the dissertation.  
