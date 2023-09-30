#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    def most_common(s):

        d = {}
        for char in s:
            d[char] = d.get(char, 0) + 1

        # Get sorted keys (sort largest to smallest + alphabetical)
        sorted_keys = sorted(d, key=lambda x: (-d[x], x))

        for i in range(3):
            print(sorted_keys[i], d[sorted_keys[i]])
    s = "zzzzzaaaaagooglellll"

    s = list(s)
    s.sort()

    print(s)



    import collections

    cnt = collections.Counter(s)

    print(cnt)
    print(*cnt)

    print(*cnt.values())
    print(*cnt.keys())

    # for item in cnt.items():
    #     print(item)

    for item in cnt.most_common():
        print(item)
