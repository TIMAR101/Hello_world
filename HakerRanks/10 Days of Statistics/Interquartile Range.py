#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#
def quartiles(arr):

    arr.sort()

    Ln = len(arr)

    if Ln % 2 == 0:
        Q1 = (arr[Ln//2] + arr[Ln//2-1])/2
        #Ln1 = Ln - 2


    else:
        Q1 = arr[Ln//2]
        Ln=Ln - 1

    if Ln % 4 == 0:
        Q2 = (arr[Ln//4] + arr[Ln//4-1])/2
        Q3 = (arr[0-Ln//4] + arr[-1-Ln//4])/2

    else:
        Q2 = arr[Ln//4]
        Q3 = arr[-1-Ln//4]

    quarlist = [Q2, Q1, Q3]

    return Q3 - Q2




def interQuartile(values, freqs):

    arr = []

    for item in range(len(values)):

        for _ in range(freqs[item]):
            arr.append(values[item])

    result = quartiles(arr)
    result = float(result)
    result = round(result, 2)

    print(result)

    # Print your answer to 1 decimal place within this function





if __name__ == '__main__':
    #n = int(input().strip())

    #val = list(map(int, input().rstrip().split()))

    #freq = list(map(int, input().rstrip().split()))

    #interQuartile(val, freq)
    interQuartile([6, 12, 8, 10, 20, 16], [5, 4, 3, 2, 1, 5])
