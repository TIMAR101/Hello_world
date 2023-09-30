import re

S = "aaadaaa"
k = "aa"

pt1 = re.compile(k)

pt2 = re.compile(fr"(?=<{k})")

# pt = re.compile(fr"(?={k})")

print(pt1.findall(S))

print(pt2.findall(S))

for item in pt2.finditer(S):

    print(item)

for item in pt1.finditer(S):

    print(item)
