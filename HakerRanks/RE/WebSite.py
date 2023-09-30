import re

p1 = re.compile(r"www\.[\w]+\.[a-zA-Z]{2,3}")

s= " This is abstraction string with two address www.ya.ru  www.timtehnol.r1u   wwww.google.com1 this is great!!!"

print(p1.match(s))

print(p1.findall(s))

print(p1.fullmatch(s))
print(p1.search(s))

for item in p1.finditer(s):
    print(item)
