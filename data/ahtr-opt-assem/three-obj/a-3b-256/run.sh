#!/bin/bash
#COBALT -t 03:30:00
#COBALT -n 256
#COBALT -q backfill
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

python -m rollo -i rollo_a_3b.json -v -c checkpoint.pkl 
