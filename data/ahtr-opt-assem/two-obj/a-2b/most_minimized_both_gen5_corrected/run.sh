#!/bin/bash
#COBALT -t 01:00:00 
#COBALT -n 4
#COBALT -q debug-flat-quad
#COBALT -A arfc-msr-ahtr

module switch PrgEnv-intel PrgEnv-gnu
module load gcc
module load cray-mpich
module load cmake
module load cray-hdf5
export CRAYPE_LINK_TYPE=dynamic
export CRAY_ADD_RPATH=yes
export CXX=CC 
export CC=cc 
export HDF5_USE_FILE_LOCKING=FALSE

module load miniconda-3
conda activate /gpfs/mira-home/gchee/openmc-env

aprun -n 1 -d 1 --env OMP_NUM_THREADS=1 python fhr_assem_openmc.py
aprun -n 4 -d 64 --env OMP_NUM_THREADS=64 openmc-0.12.2
