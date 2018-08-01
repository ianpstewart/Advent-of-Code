#! /usr/bin/env python3

print("The capatcha is: ", end = '')
inputNum = input()

capatcha = []
for num in inputNum:
    capatcha.append(num)


capatcha = [int(i) for i in capatcha]
step = int(len(capatcha) / 2)


outputSum = 0 
for num in range(-len(capatcha), 0):
     if(capatcha[num] == capatcha[num + step]):
        outputSum = outputSum + capatcha[num]



print(outputSum)
