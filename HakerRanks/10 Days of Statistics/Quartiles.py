#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
# 0 1 2 3 4 5 6 7

def quartiles(arr):

    arr.sort()

    Ln = len(arr)

    if Ln % 2 == 0:
        Q1 = (arr[Ln//2] + arr[Ln//2-1])//2
        #Ln1 = Ln - 2


    else:
        Q1 = arr[Ln//2]
        Ln=Ln - 1

    if Ln % 4 == 0:
        Q2 = (arr[Ln//4] + arr[Ln//4-1])//2
        Q3 = (arr[0-Ln//4] + arr[-1-Ln//4])//2

    else:
        Q2 = arr[Ln//4]
        Q3 = arr[-1-Ln//4]

    quarlist = [Q2, Q1, Q3]

    return quarlist




    # Write your code here


if __name__ == '__main__':

    str = "3 7 8 5 12 14 21 13 18"
    print(str)

    numlist = []

    strlist = str.split(sep= " ")
    print(strlist)
    for item in strlist:
        numlist.append(int(item))

    print(numlist)



    res = quartiles(numlist)

    print(res)


