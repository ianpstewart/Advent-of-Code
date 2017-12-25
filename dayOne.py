#! /usr/bin/env python3

inputCap = open("input.txt", "r")
capatcha=[]
for line in inputCap:
    for char in line:
        capatcha.append(char)

print(capatcha)

