#!/bin/bash
#SBATCH --job-name=simulation_v1 # Job name
#SBATCH --mail-type=ALL # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=jeku7901@colorado.edu # Where to send mail
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=23:00:00 # Time limit hrs:min:sec
#SBATCH --mem=100gb # Memory limit
#SBATCH --error=/Users/jeku7901/olwin_dowell_labs/2020_barcode_seq_run2/simulation_jupyter_sbatch/sbatch/eofiles/sim_.%j._e.txt
#SBATCH --output=/Users/jeku7901/olwin_dowell_labs/2020_barcode_seq_run2/simulation_jupyter_sbatch/sbatch/eofiles/sim_.%j._o.txt

echo Job: $SLURM_JOB_NAME with ID $SLURM_JOB_ID
echo Running on host ‘hostname’
echo Job Started at ‘date +”%T %a %d %b %y”’
echo Using $SLURM_NTASKS processors across $SLURM_NNODES nodes


python2 createallpossibilites.py
