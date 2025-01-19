#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix) // 2
    totalSum = 0

    count = 1
    count2 = 0

    for line in range(n - 1, -1, -1): # n = 3 --> range(2, 1, 0)
        y = 1
        x = 0
        
        for column in range(n - 1, -1, -1): # n = 3 --> range(2, 1, 0)
            maxElem = max(matrix[n - count][n - y], matrix[n - count][n + x], matrix[n + count2][n - y], matrix[n + count2][n + x])
            totalSum += maxElem
            y += 1
            x += 1
        count += 1
        count2 += 1

    return totalSum



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()