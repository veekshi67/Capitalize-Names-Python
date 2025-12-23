#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.

def solve(s):
    result = []
    capitalize_next = True

    for ch in s:
        if ch == ' ':
            result.append(ch)
            capitalize_next = True
        else:
            if capitalize_next and ch.isalpha():
                result.append(ch.upper())
            else:
                result.append(ch)
            capitalize_next = False

    return ''.join(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
