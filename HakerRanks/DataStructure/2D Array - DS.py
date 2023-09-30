#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):

    sum = -99999999999999999999999999

    for y in range(4):

        for x in range(1, 5):

            sum1 = arr[y][x-1] + arr[y][x] + arr[y][x+1] + arr[y+1][x] + arr[y+2][x-1] + arr[y+2][x] + arr[y+2][x+1]

            if sum1 > sum:
                sum = sum1

    return sum    # Write your code here



if __name__ == '__main__':

    MyFile=open("Input", "r")

    InputArray =[]

    for y in range(6):
        Content=MyFile.readline()
        Content = Content.replace("\n", '')
        ListSt = Content.split(sep= " ")
        for x in range(6):
            ListSt[x] = int(ListSt[x])

        InputArray.append(ListSt)

    print(InputArray)
    MyFile.close()

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(InputArray)

    print(result)


