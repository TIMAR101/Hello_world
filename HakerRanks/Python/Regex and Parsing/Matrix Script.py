#!/bin/python3

import math
import os
import random
import re
import sys




# first_multiple_input = input().rstrip().split()
#
# n = int(first_multiple_input[0])
#
# m = int(first_multiple_input[1])
#
# matrix = []
#
# for _ in range(n):
#     matrix_item = input()
#     matrix.append(matrix_item)
# data = ''
#
# for m1 in range(m):
#
#     for n1 in range(n):
#
#         data = data + matrix[n1][m1]
#
# print(data)

data = "This$#is% Matrix#  %!"
#
print(data)
ptr = re.compile(r'(?<=\w)[\s!@#$%&]+(?=\w)')

data = ptr.sub(" ", data)

print(data)

print re.sub(r'(?<=[A-Za-z0-9])([^A-Za-z0-9]+)(?=[A-Za-z0-9])',' ',"".join("".join(decode) for decode in zip(*matrix)))


s = [''.join(matrix[row][item]) for item in range(0,m) for row in range(0,n)]


s =''.join(chain(*[[matrix[x][y] for x in range(n)] for y in range(m)]))

for i in list(zip(*Matrix)):
    S += "".join(i)
