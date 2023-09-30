#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    # j = [[int(x) for x in input().split()] for _ in range(n)]

    k = int(input())

    arr.sort(key = lambda x: x[k])

    for item in arr:
        print(*item)


N, M = map(int, input().split())
rows = [input() for _ in range(N)]
K = int(input())

for row in sorted(rows, key=lambda row: int(row.split()[K])):
    print(row)

data, k = [list(map(int, input().split(' '))) for _ in range(int(input().split(' ')[0]))], int(input())
[print(*row) for row in sorted(data, key=lambda lst: lst[k])]
