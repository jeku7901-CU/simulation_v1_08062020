from __future__ import division
import itertools

outdir="/Users/jeku7901/olwin_dowell_labs/2020_barcode_seq_run2/simulation_jupyter_sbatch/outputs/"
def main():
	filenumber=0
	possible_percents = [i for i in range(0,101,5)]
 	all_percents_list = itertools.product(possible_percents, repeat = 15)
        for i in all_percents_list: 
	        list_percent_myoblasts_dividing = list(i)
		write_file = outdir+"simulation_output_" + str(filenumber) + ".csv"
		wf = open(write_file, "w")
		filenumber=filenumber+1
		line = list_percent_myoblasts_dividing
        	line = ",".join(map(str, line)) + "\n"
        	wf.write(line)
		wf.close()



if __name__ == "__main__":
    main()


