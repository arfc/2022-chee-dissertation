# AHTR One-Third Assembly Optimization, Simulation a-3b-256

The results are presented in Appendix B of the dissertation. 

This optimization simulation was run on the Theta supercomputer using the `run.sh` bash script. 
The CLI output from Theta is printed in `606930.output`. 

The `run.sh` bash script uses ROLLO to run the following input file `rollo_a_3b.json`, which also uses the following evaluator scripts:  `fhr_assem_openmc.py`, `fhr_assem_openmc_output.py`, `automate_mesh.py`, `mesh_generate.sh`, `fhr_assem_moltres.i`, `fhr_assem_moltres_output.py`, `fhr_assem_gc.inp`, and `summary_dummy.h5`.

The ROLLO output file is `checkpoint.pkl` and is analyzed using `assem_3b_256.ipynb`.

All the `*.png` figures in this directory are included in the dissertation.  

The following directories contain AHTR models that most-minimized each objective: 
`2_1`, `3_2`, and `3_81`. `0_9` contains the AHTR model that equally minimized all objectives. 