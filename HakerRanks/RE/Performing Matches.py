import re

p = re.compile('[a-z]+')

print(p.match('tempo'))

print(p.match('::: message'))

print(p.findall('::: message'))

print(p.search('::: message'))

s1 = p.search('::: message:::::message1')

s2 = p.findall('::: message:::::message1')

print(s2)

print(s1.span())

print(s1.group())

print(s1.end())

print(p.search('::: message:::::message1', s1.end()))

p3 = re.compile(r"[A-z]+")

p4 = re.compile(r"\d+")

s3 = "Threre are 2 aplles and 3 boatles on the table"

print(p3.findall(s3))

print(p4.findall(s3))





