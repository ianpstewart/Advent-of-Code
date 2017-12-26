#! /usr/bin/env python3

inputNum = input("whats the number \n")

capatcha = []
for num in inputNum:
    capatcha.append(num)
print(capatcha)

capatcha = [int(i) for i in capatcha]
print(capatcha)

outputSum = 0 
for a in range(0, len(capatcha) - 1):
     if(capatcha[a] == capatcha[a + 1]):
        outputSum = outputSum + capatcha[a]
if capatcha[0] == capatcha[-1]:
    outputSum = outputSum + capatcha[0]

print(outputSum)
