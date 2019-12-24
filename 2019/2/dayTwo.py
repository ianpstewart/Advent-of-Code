#!/usr/bin/env python3
import sys

#input.txt needs to be first argument
in_file = sys.argv[1]

code = list(map(int, open(in_file).read().split(',')))

#removes the commas and turns the values into ints

#1 adds the nums and 2 multiplies
def opcode(intcode, val1, val2):
    if intcode == 1:
        return val1 + val2

    elif intcode == 2:
        return val1 * val2

#1202 Program Alarm
#code[1] = 12
#code[2] = 2

print("The starting values are ", code)

#come in sets of four numbers


print("The final values are ", code)


