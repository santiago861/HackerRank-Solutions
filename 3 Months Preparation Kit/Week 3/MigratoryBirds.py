#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):    
    birds = {}
    for elem in arr:
        if not elem in birds:
            birds[elem] = 1
        else:
            birds[elem] += 1

    max_value = max(birds.values())
    max_elems = []
    for bird in birds:
        if birds[bird] == max_value: # birds[bird] returns the value of the element & bird returns the key of the element
            max_elems.append(bird)
    return min(max_elems)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
