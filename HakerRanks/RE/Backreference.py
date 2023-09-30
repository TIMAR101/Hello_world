import re

p=re.compile(r'\b(\w+)\s+(?:\1)\b')
print(p.search('Paris in the the spring').group())

p1 = re.compile(r"(?:abc)def")

print(p1.search("abcdef").group())
