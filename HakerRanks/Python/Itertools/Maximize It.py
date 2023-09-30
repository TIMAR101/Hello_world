"""3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10 """

"""2 24
3 24 48 96
4 24 48 96 24"""

ls = [[2,5,4],[3, 7,8,9], [5, 5, 7,8,9,10]]
import itertools

for item in range(3):

    del ls[item][0]

print(ls)

K=3
M=24

# K, M = map(int, input().split)
"""
ls = []
for __ in range(K):

ls.append(list(map(int,input().split()))"""

mx = 0

for item in itertools.product(*ls):

   mx = max(mx, (sum(a**2 for a in item))%M)


print(mx)



