#! /usr/bin/env python3
import math

#given in the question
input = 277678

closeSquare = math.sqrt(input)
closeSquare = math.ceil(closeSquare)

if closeSquare % 2 == 0:
	closeSquare += 1

diff = math.pow(closeSquare, 2) - input
mid = math.ceil(closeSquare / 2)

steps = mid + 1




