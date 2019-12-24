#!/usr/bin/env python3
import sys

#input.txt needs to be first argument
in_file = sys.argv[1]

#opens the input file and reads the every line
with open(in_file, 'r') as puzzle:
    lines = puzzle.readlines()

code = lines[0].split(",")

for position, value in enumerate(code):
    print(position, "--->>", value)
