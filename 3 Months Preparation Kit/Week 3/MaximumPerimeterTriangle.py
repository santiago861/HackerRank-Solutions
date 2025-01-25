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
    sticks.sort(reverse=True)
    # reversing the sorted array ensures to prioritize the longest posible sides, this way we find the triangle with the greates perimeter

    for i in range(0, len(sticks) - 2):
        if sticks[i] < sticks[i + 1] + sticks[i + 2]:
            return [sticks[i + 2], sticks[i + 1], sticks[i]]
    return [-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
