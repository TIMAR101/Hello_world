# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

pt = re.compile(r'ze\b')

data = "\n".join(pt.sub('se', input()) for __ in range(int(input())))

templates = [pt.sub('se', input()) for __ in range(int(input()))]

print()

for item in templates:

    print(data.count(item))








