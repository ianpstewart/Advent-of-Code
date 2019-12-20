#!/usr/bin/env python3
import sys
from math import floor 

#input.txt needs to be first argument
in_file = sys.argv[1]

#opens the input file and reads the every line
with open(in_file, 'r') as puzzle:
    lines = puzzle.readlines()

def fuelNeed(mod):
    if mod == "\n":
        return 0
    else:
        needed = floor(int(mod)/3) - 2
    
    if needed > 0:
        return needed
    else:
        return 0

total = 0
for module in lines:
        total += fuelNeed(module)

print("The sum for modules is ", total)
###############################################################################

#Part Two
total = 0
for module in lines:
    #inital fuel from module
    total += fuelNeed(module)

    #same as prevoius statement
    fuelAdd = fuelNeed(module)
    while fuelAdd > 0:
        total += fuelNeed(fuelAdd)
        fuelAdd = fuelNeed(fuelAdd)
       
print("Adjusted total is", total)

