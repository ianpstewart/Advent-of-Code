#! /usr/bin/env python3

#reads from a file named input.txt
#calculated difference between largest and smallest values

matrix = open("input.txt", 'r')

rows = [] 
checksum = 0

for line in matrix:
	strList = line.split()
	numList = list(map(int, strList))
		
	for i in range(0, len(numList)):
		for j in range(0, len(numList)):
			if ((numList[i] % numList[j] == 0) and (i != j)):
				checksum += numList[i] / numList[j]


print(checksum)
