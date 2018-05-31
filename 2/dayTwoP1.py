#! /usr/bin/env python3

#reads from a file named input.txt
#calculated difference between largest and smallest values

matrix = open("input.txt", 'r')

rows = [] 
minSum = 0
maxSum = 0

for line in matrix:
	strList = line.split()
	numList = list(map(int, strList))
	maxSum += max(numList)
	minSum += min(numList)

checksum = maxSum - minSum


print("The checksum is: ", checksum)
