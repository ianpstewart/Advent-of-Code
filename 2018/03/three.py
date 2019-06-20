#! /usr/bin/env python3

import sys

#input.txt needs to be first argument
in_file = sys.argv[1]

#opens the input file and reads the every line
with open(in_file, 'r') as puzzle:
    lines = puzzle.readlines()

#1000x1000 array of zeros
sheet = [[0 for i in range(0,1000)] for j in range(0,1000)]

xRange = []
yRange = []
for line in lines:
    x = [0, 0]
    y = [0, 0]
    items = line.split()
    x[0] = items[2].split(",")[0]
    y[0] = items[2].split(",")[0]
    x[1] = x[0] + items[3].split("x")[0]
    y[1] = y[0] + items[3].split("x")[0]

    
