#! /usr/bin/env python3

from collections import defaultdict as defaultdict

def checkPhrase(line):
    result = defaultdict(int)
    words = line.split(" ") 
    for val in words:
        val = val.rstrip()
        result[val] += 1

    for val in result.values():
        if val > 1:
            return 0
    return 1
        
validLine = 0

with open("input.txt") as file:
    for line in file:
        if checkPhrase(line):
            validLine += 1

print(validLine)
