# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

import collections

ordict = collections.OrderedDict()

cnt = collections.Counter()

words = [input() for _ in range(n)]

print(words)

cnt.update(words)



print(cnt)
print(*cnt)

print(*cnt.keys())

print(*cnt.values())

for word in words:

    ordict[word] = ordict.get(word, 0) + 1

print(ordict)
print(*ordict)

print(*ordict.keys())
print(*ordict.values())

# print(ordict.__len__())
#
# for item in ordict.values():
#     print(item, end= " ")
#
# print(*ordict.values())
