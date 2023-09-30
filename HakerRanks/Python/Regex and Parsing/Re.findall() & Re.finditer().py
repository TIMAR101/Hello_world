import re
c=re.finditer(r'(\w)','http://www.hackerrank.com/')



m = map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
#['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

# print(m)
#
# print(list(m))

ptr = re.compile(r"(?:[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([euioaEUIOA]{2,})(?:[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])")

data = "abaabaabaabaae"

print(ptr.findall(data))

pos = 0

s1 = ptr.search(data, pos)

if s1:

    while s1:

        print(s1.group(1))
        pos = s1.end() - 1
        s1 = ptr.search(data, pos)




else:

    print("-1")








