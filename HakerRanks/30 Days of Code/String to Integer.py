#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    S = input()
    try:
        print(f'{int(S)}')
    except ValueError as ve:
        print(f'Bad String')

