#!/usr/bin/env python3
import sys

#input.txt needs to be first argument
in_file = sys.argv[1]

code = list(map(int, open(in_file).read().split(',')))

#removes the commas and turns the values into ints

#1 adds the nums and 2 multiplies
def opcode(intcode, val1, val2):
    if intcode == 1:
        print("\tAdd ", code[val1] + code[val2])
        return code[val1] + code[val2]

    elif intcode == 2:
        print("\tMultiply ", code[val1], "and ", code[val2])
        print(code)
        return code[val1] * code[val2]


#1202 Program Alarm
code[1] = 12
code[2] = 2

print("The starting values are ", code)

#come in sets of four numbers
pos = 0
while True:
    if code[pos] == 99:
        print("done") 
        break
    else:
        replace = code[pos + 3]
        print("\treplace value ", replace, "in position ", pos + 3)
        code[replace] = opcode(code[pos], code[pos + 1], code[pos + 2])
        pos += 4


print("The final values are ", code)


