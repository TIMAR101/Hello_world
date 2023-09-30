#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    a = "         1 2 3 4 5 100 99 0              "
    print(a, "///")
    b = a.split()
    print(b, "///")
    c = map(int, b)
    print(list(c))

    # a = input().rstrip()
    # print(a)
    #
    arr = []

    file = open("Input 2D Arrara", mode="r+t")

    a = file.readlines()
    print(a)
    for item in range(len(a)):
        a[item] = list(map(int, a[item].replace('\n', '').split()))

    print(a)
    arr = a.copy()

    # print(a)
    # b = map(int, a)
    # print(b)
    # c = list(b)

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))
    #     print(arr)

    len1 = len(arr)
    len2=len(arr[0])
    hourglass = []

    for item1 in range(len1-2):

            for item2 in range(len2-1):

                elem = sum(arr[item1][item2: item2 + 3]) + sum(arr[item1+2][item2: item2 + 3]) + arr[item1+1][item2+1]

                hourglass.append(elem)



    print(max(hourglass))
