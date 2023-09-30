# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
pattern = re.compile(r'(?<=\s)(&&|\|\|)(?=\s)')
for _ in range(n):
    print(re.sub(pattern,lambda x: 'and' if x.group(0)=='&&' else 'or',input()))"""

import re


data = "\n".join(input() for __ in range(int(input())))


data=re.sub(r"(?<=\s)&&(?=\s)", "and", data)

data=re.sub(r"(?<=\s)\|\|(?=\s)", "or", data)

print(data)
