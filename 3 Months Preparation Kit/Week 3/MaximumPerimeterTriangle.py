#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here

    # A non-degenerate triangle is one where the sum of the lengths of any two sides is greater than the length of the remaining side.
    # we need to discard the triangles which the sum between 2 of its sides is less or equal to the third side
    sticksInOrder = sorted(sticks)
    triangles = []
    for i in range(0, len(sticksInOrder) - 2):
        if sticksInOrder[i] + sticksInOrder[i + 1] > sticksInOrder[i + 2]:
            triangles.append([sticksInOrder[i], sticksInOrder[i + 1], sticksInOrder[i + 2]])

    max_sides = []
    min_sides = []
    
    if len(triangles) == 0:
        return [-1]
    elif len(triangles) > 1:
        for triangle in triangles:
            max_sides.append(max(triangle))
            min_sides.append(min(triangle))
        if max_sides.count(max(max_sides)) == 1:
            return triangles[max_sides.index(max(max_sides))]
        elif max_sides.count(max(max_sides)) > 1:
            return triangles[min_sides.index(max(min_sides))]
        else:
            return triangles[0]
    else:
        return triangles[0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
