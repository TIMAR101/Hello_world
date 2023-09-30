# """>> myset.add('c')
# >> myset
# {'a', 'c', 'b'}
# >> myset.add('a') # As 'a' already exists in the set, nothing happens
# >> myset.add((5, 4))
# >> myset
# {'a', 'c', 'b', (5, 4)}"""
#
# myset = {'a', 'c', 'b'}
#
# print(myset)
#
# myset.add((5, 4))
#
# print(myset)
#
# myset.update([1,2,3])
#
# print(myset)
#
# myset.remove(1)
# print(myset)
#
# myset.discard(2)
# print(myset)
#
# myset.discard(2)
# print(myset)
#
# """>> a = {2, 4, 5, 9}
# >> b = {2, 4, 11, 12}
# >> a.union(b) # Values which exist in a or b
# {2, 4, 5, 9, 11, 12}
# >> a.intersection(b) # Values which exist in a and b
# {2, 4}
# >> a.difference(b) # Values which exist in a but not in b
# {9, 5}"""
#
# a = {2, 4, 5, 9}
#
# b = {2, 4, 11, 12}
#
# print(a.union(b))
#
# print(a)
#
# print(a.intersection(b))
#
# print(a)
# print(a.difference(b))

M = input()

Mset = set(map(int, input().split()))

N = input()

Nset = set(map(int, input().split()))

dif = []

dif = sorted(list(Mset.difference(Nset)) + list(Nset.difference(Mset)))

for item in dif:
    print(item)




