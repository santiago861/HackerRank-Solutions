#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zero = 0
    
    for i in arr:
        if i > 0: 
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    
    positive = positive / len(arr)
    negative = negative / len(arr)
    zero = zero / len(arr)
    
    # positive = round(positive, 6)
    # negative = round(positive, 6)
    # zero = round(positive, 6)
    print(positive)
    print(negative)
    print(zero)

        
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
