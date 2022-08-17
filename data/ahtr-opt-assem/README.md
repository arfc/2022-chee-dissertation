# AHTR One-Third Optimization 

The results are presented in Chapters 5 and 7 of the dissertation. 

`computational_cost_assem.ipynb` summarizes the Theta computational cost taken by each one-third assembly optimization problem. 

`find_out_pf.ipynb` calculates the packing fraction in the one-third assembly problem. 

`htc_calc_one_third_assem.ipynb` calculates the heat transfer coefficient for the one-third assembly's Moltres temperature model. 

`/verification/` provides data and results for the AHTR one-third assembly verification studies conducted in Chapter 5. 

`/single-obj/`, `/two-obj/`, and `/three-obj/` provide the data and results for the AHTR plank optimization simulations conducted in Chapter 7. 

Reproducing the results generated in this directory requires installation of the following software: 

```
ROLLO: https://github.com/arfc/rollo

Moltres: https://github.com/arfc/moltres

OpenMC: https://github.com/openmc-dev/openmc
```
and downloading of the following repositories (due to script dependencies).
```
fhr-benchmark repo: https://github.com/arfc/fhr-benchmark

moltres repo: https://github.com/arfc/moltres
```