import re

p = re.compile('(ab)*')
print(p.match('ababababab').span())

m = p.match('ababababab')

print(m.groups())

print(m.group(0, 1))

p = re.compile('(a(b)c)d')
m = p.match('abcd')

print(m.group(1))

p = re.compile(r'\b(\w+)\s+\1\s+\1\b')
m = p.search('Paris in the the the spring')

print(m.group())

p1 = re.compile(r"\b(\w+)\1\b")

print(p1.search("Paris in the the the  codecode thethe spring"))

print(p1.findall("Paris in the the the  code thethe spring"))

p1 = re.compile('(ab)*')

p2 = re.compile(r"[ab]*")
print(p1.match('ababababab').span())

print(p2.match('ababababab').span())

p = re.compile('(a)(b)')
m = p.match('ab')
print(m.group())

print(m.group(0))

print(m.group(1))

print(m.group(2))
print(m.groups())


