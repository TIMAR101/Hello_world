from collections import Counter

X =int(input())

ShoeSizes  = list(map(int, input().split()))
N = int(input())
# List1 = [[l, g] for l in range(4) for g in range(4) if l < 2 and g > 2]
CustomRequest = [[0, 0] for _ in range(N)]

for item in range(N):
    Request = list(map(int, input().split()))
    CustomRequest[item] = Request

DictShoeSize = Counter(ShoeSizes)
Sum = 0

for item in CustomRequest:
    if item[0] in DictShoeSize.keys() and DictShoeSize[item[0]] > 0:
        Sum += item[1]
        DictShoeSize[item[0]] -= 1

print(Sum)








