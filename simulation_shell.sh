#!/bin/bash
#SBATCH --job-name=simulation_some_poss # Job name
#SBATCH --mail-type=ALL # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=jeku7901@colorado.edu # Where to send mail
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=23:00:00 # Time limit hrs:min:sec
#SBATCH --mem=10gb # Memory limit
#SBATCH --error=/Users/jeku7901/olwin_dowell_labs/2020_barcode_seq_run2/simulation_jupyter_sbatch/eofiles/%j._e.txt
#SBATCH --output=/Users/jeku7901/olwin_dowell_labs/2020_barcode_seq_run2/simulation_jupyter_sbatch/eofiles/%j._o.txt

python2 simulation_v3.py \
/scratch/Users/jeku7901/simulation_update/sim_possibilities_outputs/sim_some_possibilities_50m.csv \
/scratch/Users/jeku7901/simulation_update/sim_outputs/sim_50m_96hrs_1musc_trans29_percmybdiv.csv
