import re

ptr = re.compile(r"(\d{3})(\d{3})")

data = "123456"

print(ptr.findall(data))

print(ptr.sub(r'\2\1', data))


ls = [1,2,3,4,5,6,7,8,9]


for item in ls.copy():

    if item % 2 == 0:

        ls.append(item + 2)

print(ls)


