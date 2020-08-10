from __future__ import division
import itertools


def main():
	filenumber=0
	possible_percents = [i for i in range(0,101,5)]
 	all_percents_list = itertools.product(possible_percents, repeat = 15)
        for i in all_percents_list: 
	        list_percent_myoblasts_dividing = list(i)
		write_file = "simulation_out/simulation_output_" + str(filenumber) + ".csv"
		wf = open(write_file, "w")
		filenumber=filenumber+1
		line = list_percent_myoblasts_dividing
        	line = ",".join(map(str, line)) + "\n"
        	wf.write(line)
		wf.close()



if __name__ == "__main__":
    main()


