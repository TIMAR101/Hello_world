""" print zip([1,2,3,4,5,6],'Hacker')
[(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]

print zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
[(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]

A = [1,2,3]
B = [6,5,4]
C = [7,8,9]
X = [A] + [B] + [C]

print zip(*X)
[(1, 6, 7), (2, 5, 8), (3, 4, 9)]"""

A = [1,2,3]
B = [6,5,4]
C = [7,8,9]
X = [A] + [B] + [C]
print(X)

print(list(zip(*X)))

# Enter your code here. Read input from STDIN. Print output to STDOUT

N, X = map(int, input().split())

ls = []
ls = [map(float, input().split()) for _ in range(X)]


print(ls)
print(list(zip(*ls)))

print((sum(item)/X for item in list(zip(*ls))), sep="/n")

for n in (sum(item)/X for item in list(zip(*ls))):
    print(n)

print(*[sum(item)/X for item in list(zip(*ls))], sep="\n")


"""n, x = map(int, input().split())

for s in zip(*[map(float, input().split()) for _ in range(x)]):
    print(f'{sum(s)/x:1.1f}')"""


