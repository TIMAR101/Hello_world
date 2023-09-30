import itertools

""">>> from itertools import permutations
>>> print permutations(['1','2','3'])
<itertools.permutations object at 0x02A45210>
>>> 
>>> print list(permutations(['1','2','3']))
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
>>> 
>>> print list(permutations(['1','2','3'],2))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
>>>
>>> print list(permutations('abc',3))
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]"""


print(list(itertools.permutations("abc", 2)))

st, b = input().split()


ls = list("".join(item) for item in itertools.permutations(st, int(b)))

ls.sort()



for item in ls:
    print(item)




# for item in itertools.permutations(st, int(b)):
#
#     res= ""
#
#     for ch in item:
#
#         res+=ch
#
#     print(res)



