#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    nBin = bin(n)
    nBin = str(nBin[2:])
    while len(nBin) < 32:
        nBin = '0' + nBin
    switched = ''
    for char in nBin:
        if char == '1':
            switched += '0'
        elif char == '0':
            switched += '1'
    bDec = int(switched, 2)
    return bDec


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
