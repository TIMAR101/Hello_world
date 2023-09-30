#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    # n = int(input().strip())
    #
    # a = list(map(int, input().rstrip().split()))
    a = [3, 2, 1]
    print(a)

    swaps = 0

    # Write your code here

    """for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }
    
    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}"""
    len_a=len(a)


    for item1 in range(len_a):

        numberOfSwaps = 0


        for item2 in range(len_a-1):
            if a[item2]> a[item2+1]:
                swaps += 1
                a[item2], a[item2+1] = a[item2+1], a[item2]
                numberOfSwaps += 1
                print(a)

        if numberOfSwaps == 0:
            break

    """Array is sorted in 5 swaps.
    First Element: 1
    Last Element: 4"""
    print(f"Array is sorted in {numberOfSwaps} swaps")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
    print(a)
    print(swaps)


