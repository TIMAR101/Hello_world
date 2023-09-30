# Enter your code here. Read input from STDIN. Print output to STDOUT

import re


ptr=re.compile(r"^[+-]?\d*[\.][\d]+$")

print(ptr.match("4.0O0"))
