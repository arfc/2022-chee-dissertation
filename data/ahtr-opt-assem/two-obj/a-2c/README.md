# AHTR One-Third Assembly Optimization, Simulation a-2c

The results are presented in Section 7.3.3 of the dissertation. 

This optimization simulation was run on the Theta supercomputer using the `run.sh` bash script. 
The CLI output from Theta is printed in `604733.outputt`. 

The `run.sh` bash script uses ROLLO to run the following input file `rollo_a_2c_temp_ppf.json`, which also uses the following evaluator scripts:  `fhr_assem_openmc.py`, `fhr_assem_openmc_output.py`, `fhr_assem.geo`, 
`fhr_assem.msh`, `fhr_assem_moltres.i`, `fhr_assem_moltres_output.py`, 
`fhr_assem_gc.inp`, and `summary_dummy.h5`.

The ROLLO output file is `checkpoint.pkl` and is analyzed using `assem_two_obj_2c.ipynb`.

All the `*.png` figures in this directory are included in the dissertation.  
