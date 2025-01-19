#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min = scores[0]
    max = scores[0]
    timesMin = 0
    timesMax = 0
    timesBrokeRecord = []

    for score in scores[1:]:
        if score > max:
            timesMax += 1
            max = score
        elif score < min:
            timesMin += 1
            min = score
        else:
            continue
        
    timesBrokeRecord.append(timesMax)
    timesBrokeRecord.append(timesMin)

    return timesBrokeRecord

# 10 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
