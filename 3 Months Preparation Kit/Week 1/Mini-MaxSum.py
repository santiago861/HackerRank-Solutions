
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min = 0
    max = 0

    arr = sorted(arr)

    for i in arr[0: 4]:
        min += i
    for j in arr[1: 5]:
        max += j
    
    print(f'{min} {max}')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
