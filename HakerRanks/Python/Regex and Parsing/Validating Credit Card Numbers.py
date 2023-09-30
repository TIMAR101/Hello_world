# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

ptr = re.compile(r'^(?!.*(\d)(-?\1){3})[4-6][\d]{3}(-?\d{4}){3}$')

# pattern=re.compile(r'^(?!.*(\d)(-?\1){3,})[456]\d{3}(?:(-?[\d]{4})){3}$')


for __ in range(int(input())):

    data = input()

    if ptr.fullmatch(data):
        print("Valid")
    else:
        print("Invalid")
