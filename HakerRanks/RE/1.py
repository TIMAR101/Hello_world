import re
p = re.compile("[a-z]+")
print(p)
print(p.match(""))

m = p.match("tempo")
print(m)


print(m.group())
print(m.start(), m.end())
print(m.span())

print(p.match("::::message"))

s = p.search("::::: message")
print(s)
print(s.span())

p = re.compile("\w+")
m = p.findall("string goes here")
print(m)

p1 = re.compile(r'\S+')
p2 = re.compile("\w+")
print(p1.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping'))
print(p2.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping'))

print(re.match(r"From\s*", "Fromage amk"))


