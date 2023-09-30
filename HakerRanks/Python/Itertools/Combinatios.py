""">>> from itertools import combinations

print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]

>A = [1,1,3,3,3]
>>print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]"""

import itertools

print(list(itertools.combinations("1234", 2)))
# print(list(itertools.permutations("1234", 2)))
# print(list(itertools.product("1234", repeat= 2)))

# A = [1,1,3,3,3]
# print( list(itertools.combinations(A,4)))
#
# print( list(itertools.permutations(A,4)))

from itertools import combinations

st, b = input().split()



for comb in range(1, int(b)+1):

    ls = list((list(item)) for item in combinations(st,comb))
    for item in range(len(ls)):
        ls[item].sort()
    ls.sort()

    #print(ls)

    for item in ls:
        #item.sort()
        print("".join(item))


"""A
C
H
K
AC
AH
AK
CH
CK
HK"""


