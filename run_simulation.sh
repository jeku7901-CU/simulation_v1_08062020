outfiledir=/scratch/Users/jeku7901/sim_output/
indir=/scratch/Users/jeku7901/sim_possibilities_output/

for path_filename in `ls ${indir}*.csv`;do
        rootname=`basename $path_filename`
	outfilename=${outfiledir}$rootname
	sbatch --export=filename=$path_filename,outfilename=$outfilename simulation_v2.sh
	echo $path_filename	
	wait 300 # this is in seconds so adjust for how long it takes
done 
