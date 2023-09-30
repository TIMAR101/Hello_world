import re

p = re.compile(r'\W+')

s1 = "1 877 2638277"

s2 = '91-011-23413627'
print(p.split(s2))

pattern = re.compile(r'(?:\d{1,3})[- ](\d{1,3})[- ](\d{4,10})')

pattern1 = re.compile(r'(?P<Country>\d{1,3})[- ](?P<Region>\d{1,3})[- ](?P<Phone>\d{4,10})')  #(?P<name>...)

res = pattern1.match(s2)

print(res)

print(res.group("Country"))

print(res.group("Region"))
print(res.group("Phone"))






