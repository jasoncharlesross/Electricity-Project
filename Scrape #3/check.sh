#!/bin/bash

#SBATCH --job-name=gas_data
#SBATCH --output=gas_data.out
#SBATCH --error=gas_data.err
#SBATCH --time=36:00:00
#SBATCH --partition=bigmem2
#SBATCH --ntasks=1
#SBATCH --mem=64G
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jasonross@uchicago.edu

module load R

# Use R CMD BATCH to run gas_scr.
R CMD BATCH --no-save --no-restore check.R