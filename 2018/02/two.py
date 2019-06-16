#! /usr/bin/env python3

import sys

def findRepeated(line):
    twos = 0
    threes = 0
    tally = {}
    for letter in line:
        if letter not in tally.keys():
            tally[letter] = 1
        elif letter in tally.keys():
            tally[letter] +=1

    for item in tally.item():
        if item < 2:
            threes += 1
        elif item < 1:
            twos += 1

    return twos, threes

#input.txt needs to be first argument
in_file = sys.argv[1]

#opens the input file and reads the every line
with open(in_file, 'r') as puzzle:
    lines = puzzle.readlines()

total2 = 0
total3 = 0
for line in lines:
    twos, threes = findRepeated(line)
    total2 += twos
    total3 += threes

checksum = total2 * total3

print(checksum)
