#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
for item in range(1,11):
    result = n * item
    #ss = "Hello {0}. You are the next {1}".format(fn, sn)
    ss = "{0} x {1} = {2}".format(n, item, result)

    print(ss)
    print()
