#! /usr/bin/env python3
import math

#given in the question
input = 277678


#defines the number at the bottom right of the square
#will always be a sqaure of a odd number
closeSquare = math.sqrt(input)
closeSquare = math.ceil(closeSquare)
if closeSquare % 2 == 0:
	closeSquare += 1

#defines each corner of the square
corners = [] 
for i in range(0, 5):
    corners.append(pow(closeSquare, 2) - (i * (closeSquare - 1)))

#defines the input's distance from each corner
diffCorners = []
for  pos, val in enumerate(corners):
    diffCorners.append(abs(input - val))

#one leg of the distnace will always be measured
#from the edge of the square
maxDis = (2 * int(closeSquare / 2))

totalDis = maxDis - min(diffCorners)

print("Max: {0}".format(maxDis))

print(totalDis)


