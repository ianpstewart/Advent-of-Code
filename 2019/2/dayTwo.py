#!/usr/bin/env python3
import sys

#input.txt needs to be first argument
in_file = sys.argv[1]

#opens the input file and reads the every line
with open(in_file, 'r') as puzzle:
    lines = puzzle.readlines()

code = list(lines[0])

def opcode(intcode, pos):
    if intcode[pos] == 1:
        sum = intcode[pos + 1] + intcode[pos + 2]
    elif intcode[pos] == 2:
        prod = intcode[pos + 1] + intcode[pos + 2]

#1202 Program Alarm
code[1] = 12
code[2] = 2

for position, value in enumerate(code)
    if position % 3 != 0:
        continue
    elif value == 99:
        break
    else:
        code[position + 3] = opcode(code, position)

print("The final value in position 0 is", code[0])
