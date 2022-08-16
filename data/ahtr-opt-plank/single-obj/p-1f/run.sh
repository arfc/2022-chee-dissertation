#!/bin/bash
#COBALT -t 2:00:00
#COBALT -n 128
#COBALT -q default
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

python ../../../../rollo/rollo -i rollo_coolant_ppf.json -c checkpoint.pkl |& tee -a results.txt
