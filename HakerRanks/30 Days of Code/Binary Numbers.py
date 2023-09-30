#!/bin/python3

import math
import os
import random
import re
import sys

def quantofdigits(num):

    s = str(bin(num))
    print(s)
    count = 0
    ListCount = []

    for item in s:

        if item == "1":
            count += 1
        else:
            ListCount.append(count)
            count = 0
    ListCount.append(count)

    print(ListCount)
    print(max(ListCount))


if __name__ == '__main__':
    n = int(input().strip())

    quantofdigits(n)

