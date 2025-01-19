#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    changedLetters = 0
    start = 0
    end = 3

    while end <= len(s):
        if s[start:end] != 'SOS':
            if s[start] != 'S':
                changedLetters += 1

            if s[start + 1] != 'O':
                changedLetters += 1

            if s[end - 1] != 'S':
                changedLetters += 1

        start += 3
        end += 3
    return changedLetters

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
