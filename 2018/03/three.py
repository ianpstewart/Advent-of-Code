#! /usr/bin/env python3

import sys
import squaresTwo

#input.txt needs to be first argument
in_file = sys.argv[1]

#opens the input file and reads the every line
with open(in_file, 'r') as puzzle:
    lines = puzzle.readlines()

square = squaresTwo.squaresTwo(43, 43)
square.coords()
