# FHR Benchmark Temperature Model 

The results are presented in Section 3.4 of the dissertation. 

`benchmark_knp.ipynb` generates the key neutronics parameters verification study results presented in the dissertation's Section 3.4.1. 

`mesh_refinement.ipynb` generates mesh refinement study results presented in the dissertation's Section 3.4.2. 

The `/moltres/` directory contains the Moltres temperature model results presented in the dissertation's Section 3.4.3. 
Specifically, `benchmark_moltres_exodus.e` contains the reported Moltres temperature distribution. 

Reproducing the results generated in this directory requires installation of the following software: 

Moltres: https://github.com/arfc/moltres

OpenMC: https://github.com/openmc-dev/openmc

and downloading of the following repositories (due to script dependencies).

fhr-benchmark repo: https://github.com/arfc/fhr-benchmark

moltres repo: https://github.com/arfc/moltres

