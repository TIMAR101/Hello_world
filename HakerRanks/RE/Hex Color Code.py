# Enter your code here. Read input from STDIN. Print output to STDOUT

import re


#symbols = "1234567890abcdefABCDEF"
with open('Hex Color Code.txt', mode='r') as f:
    data = f.read()

ptr = re.compile(r"(?<=[: ])#[0-9a-fA-F]{3,6}")

inside_brackets = re.findall(r'\{.*?\}', data, flags=re.DOTALL)
print(inside_brackets)
for property in inside_brackets:
    map(lambda i: print(i,sep='\n',end='\n'),(re.findall(r'#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})\b', property)))

# print(ptr.findall(data))
#
# for item in ptr.findall(data):
#     print(item)





