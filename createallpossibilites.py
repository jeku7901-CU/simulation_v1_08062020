from __future__ import division
import itertools

#outdir="/Users/jeku7901/olwin_dowell_labs/2020_barcode_seq_run2/simulation_jupyter_sbatch/outputs/"
outdir="/scratch/Users/jeku7901/sim_possibilities_output/"
def main():
	filenumber=0
	possible_percents = [i for i in range(0,101,10)]
 	all_percents_list = itertools.product(possible_percents, repeat = 15)
        lines=[]
	n=0
	for i in all_percents_list: 
	        if n==0:
                	write_file = outdir+"simulation_output_" + str(filenumber) + ".csv"
                        wf = open(write_file, "w")
		n=n+1
		list_percent_myoblasts_dividing = list(i)
		line = list_percent_myoblasts_dividing
		line = ",".join(map(str, line)) + "\n"
		lines.append(line)
		if len(lines)==1000:
                        for line in lines:
                                wf.write(line)
                        lines=[]
		if n==100000000000:
			filenumber=filenumber+1
			wf.close()
                        write_file = outdir+"simulation_output_" + str(filenumber) + ".csv"
                        wf = open(write_file, "w")
			n=0
			break
        for line in lines:
        	wf.write(line)
        wf.close()
       




if __name__ == "__main__":
    main()


