#!/bin/bash
#COBALT -t 01:00:00 
#COBALT -n 1
#COBALT -q debug-cache-quad
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

aprun -n 64 -N 64 -d 1 -j 1 moltres-opt -i fhr_assem_moltres.i
