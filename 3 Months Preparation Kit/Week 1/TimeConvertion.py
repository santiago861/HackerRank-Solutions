#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    if 'PM' in s:
        first = int(s[0:2])
        
        if first <= 11:
            s = s[2:-2]
            first = first + 12
            finalPM = str(first) + s
            return finalPM
        else:
            return s[0:-2]
    elif 'AM' in s:
        first = s[0:2]
        if first == '12':
            string = s[2:-2]
            s = '00' + string
            return s
        else:
            return s[0:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
