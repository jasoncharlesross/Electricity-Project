#!/bin/sh
#SBATCH --partition=bigmem2
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=64G

module load python
python merge.py