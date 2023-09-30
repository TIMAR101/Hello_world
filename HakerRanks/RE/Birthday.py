import re
# pattern = re.compile("^[\\w-]+@[0-9a-zA-Z]+\\.[a-z]{1,3}$")
#p = re.compile(r'[\d]{1,2}+\.[\d]{1,2}+\.[\d]{2,4}')
p = re.compile(r'[\w_-]+@[\w]+\.[a-zA-Z]{1,3}$')

p1 = re.compile(r'[0-3][\d]\.[0-1][\d]\.[1-2][\d]{1,3}')

s= "Timofey's birtdhay is 25.09.1984. It's great!!! Irina's birtdhay is 04.04.1991 Aliya's birthday is 08.09.1991 Wrong birthday 99.25.1990"


m1 = p1.search(s)




print(p1.findall(s))

print(p1.fullmatch(s))
print(p1.search(s))

for item in p1.finditer(s):
    print(item)



