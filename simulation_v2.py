from __future__ import division
import itertools

def initiate_cells_per_myofiber(number_of_stemcells = 5, number_of_myoblasts = 0):
    cells = []

    for cell in range(number_of_stemcells):
        cells.append("sc")

    for cell in range(number_of_myoblasts):
        cells.append("my")

    return cells

def divisionrate(cells, percent_stemcells_dividing = 100, percent_myoblasts_dividing = 100):
   # print(percent_stemcells_dividing, percent_myoblasts_dividing)
    number_of_stemcells = cells.count("sc")  #len([cell for cell in cells if cell == "sc"])
    number_of_myoblasts = cells.count("my")  #len([cell for cell in cells if cell == "my"])

    subset_of_stemcells = number_of_stemcells * (percent_stemcells_dividing / 100)
    subset_of_myoblasts = number_of_myoblasts * (percent_myoblasts_dividing / 100)

    subset_of_stemcells = int(round(subset_of_stemcells))
    subset_of_myoblasts = int(round(subset_of_myoblasts))
    
    #print(subset_of_stemcells, subset_of_myoblasts)


    for cell in range(subset_of_stemcells):
        cells.append("sc")

    for cell in range(subset_of_myoblasts):
        cells.append("my")

    return cells

def sc_to_myb_function(cells, percent_transmutation_sc = 20): # percent sc's per myofiber turning into myoblasts
    subset_of_stemcells = cells.count("sc")
    subset_of_stemcells = subset_of_stemcells * (percent_transmutation_sc / 100)
    subset_of_stemcells = int(round(subset_of_stemcells))
    for cell in range(subset_of_stemcells):
        i = cells.index("sc")
        cells[i] = "my"
    return cells

max_div = 15 
list_percent_myoblasts_dividing = []

def masterdivision_function(cells, total_hrs = 120, subsequent_div_hrs = 8, max_div = max_div, list_percent_myoblasts_dividing = list_percent_myoblasts_dividing): #5 days = 120hrs
    # this is division#1
   #print("before_first_div",list_percent_myoblasts_dividing, cells)
    total_hrs = total_hrs - 30
    cells = divisionrate(cells, 20, 0)
    cells = sc_to_myb_function(cells, 29)
    #print("fter_1st_div", cells)
    # to make sure cells stop dividing after total_hrs is over
    for i,div in enumerate(range(max_div)):
        if total_hrs < 0:
            return cells
        else:

    # this is for subsequent divisions
            percent_myoblasts_dividing = list_percent_myoblasts_dividing[i]
            total_hrs = total_hrs - subsequent_div_hrs
            cells = divisionrate(cells, 0, percent_myoblasts_dividing) # Only the initial myoblasts are dividing (at 100%)
            cells = sc_to_myb_function(cells, 0)
    return cells

def main_function(inputfile):
    #print("starting")
    wf = open(inputfile, "r")
    line=wf.readline()
    line=line.strip("\n")
    list_percent_myoblasts_dividing=line.split(",")
    wf.close()
    wf = open(inputfile, "w")

    cells = initiate_cells_per_myofiber()    
    cells = masterdivision_function(cells, list_percent_myoblasts_dividing = list_percent_myoblasts_dividing)
    line = [cells.count("my"), cells.count("sc")] + list_percent_myoblasts_dividing
    line = ",".join(map(str, line)) + "\n"
    wf.write(line)
    wf.close()

if __name__ == "__main__":
	inputfile=sys.argv[1]
	main_function(inputfile)
