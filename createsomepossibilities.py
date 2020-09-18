from __future__ import division
import itertools
import random

#outdir="/Users/jeku7901/olwin_dowell_labs/2020_barcode_seq_run2/simulation_jupyter_sbatch/outputs/"
outdir="/scratch/Users/jeku7901/sim_possibilities_output/"

def random_product(*args, repeat=1):
	"Random selection from itertools.product(*args, **kwds)" 
	pools = [tuple(pool) for pool in args] * repeat
	return list(random.choice(pool) for pool in pools)

def main():
	filenumber=0
	possible_percents = [i for i in range(0,101,10)]
	lines=[]
	n=0
	wf=open(outdir+"sim_some_possibilities.csv", "w")
	for i in range(0,100000):
		line=random_product(possible_percents, repeat=15)
		line = ",".join(map(str, line)) + "\n"
		lines.append(line)
		if len(lines)==10000:
			for line in lines:
				wf.write(line)
			lines=[]
	for line in lines:
		wf.write(line)
	wf.close()
	


if __name__ == "__main__":
    main()


