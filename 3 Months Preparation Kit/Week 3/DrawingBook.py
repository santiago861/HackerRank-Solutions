#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    if p == n or (n - 1 == p and n % 2 == 1) or p == 1:
        return 0
    
    rev = 0
    if n % 2 == 0:
        rev = math.ceil((n - p) / 2)
    else: 
        rev = math.floor((n - p) / 2)
    
    return min(p//2, rev) # the first argument is the result from page 1 to end & the 2nd is the result from end to start

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
