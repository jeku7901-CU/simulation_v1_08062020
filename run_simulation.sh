
indir=/Users/jeku7901/olwin_dowell_labs/2020_barcode_seq_run2/simulation_jupyter_sbatch/outputs/

for path_filename in `ls ${indir}*.csv`;do
	sbatch --export=filename=$path_filename simulation_v2.sh
	echo $path_filename	
	wait 1 

done 
