#! /usr/bin/env python3

#This is the first challenge for 2018

import sys
import itertools

#starting at zero take the input file and find the final frequency. sums all the
#numbers
#first argument is the input file
in_file = sys.argv[1]

#opens the input file and reads the every line
with open(in_file, 'r') as puzzle:
    lines = puzzle.readlines()

current_freq = 0

for line in lines:
    current_freq += int(line)

print(f"the current frequency is {current_freq}")

################################################################################
#reset the frequency
current_freq = 0
previous_freq = {0}

for line in itertools.cycle(lines):
    current_freq += int(line)
    if current_freq in previous_freq:
        print(f"first duplicate is {current_freq}")
        break
    previous_freq.add(current_freq)
