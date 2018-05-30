#! /usr/bin/env python3

print("The capatcha is: ", end = '')
inputNum = input()

capatcha = []
for num in inputNum:
    capatcha.append(num)


capatcha = [int(i) for i in capatcha]


outputSum = 0 
for a in range(0, len(capatcha) - 1):
     if(capatcha[a] == capatcha[a + 1]):
        outputSum = outputSum + capatcha[a]

if capatcha[0] == capatcha[-1]:
    outputSum = outputSum + capatcha[0]

print(outputSum)
