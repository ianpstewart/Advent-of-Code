#! /usr/bin/env python3

import sys

def findRepeated(line):
    twos, threes = 0, 0
    isTwo, isThree = False, False

    tally = {}
    #sees if the leter has occured before and adds one
    for letter in line:
        if letter not in tally.keys():
            tally[letter] = 1
        elif letter in tally.keys():
            tally[letter] += 1
    #if there are more than two letters that are repeated multiple times this
    #ignores them.
    for item in tally.values():
        if item == 3:
            isThree = True
        elif item == 2:
            isTwo = True

    if isThree:
        threes += 1
    if isTwo:
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
################################################################################
#part 2
sames = []

#checks each pair twice :( also ignoring newlines
for line1 in lines:
    for line2 in lines:
        diff = 0
        for i in range(0, len(line1)):
            if line1[i] != line2[i]:
                diff += 1
        if diff == 1:
            print(f"{line1} and {line2} are the ones")
            for i in range(0, len(line1)):
                if line1[i] == line2[i]:
                    sames.append(line1[i])

            for letter in sames:
                print(letter, end="")
