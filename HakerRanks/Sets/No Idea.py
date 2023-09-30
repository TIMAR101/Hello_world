n, m = map(int, input().split())

m = list(map(int, input().split()))

A = set(map(int, input().split()))

B = set(map(int, input().split()))

print(sum((item in A) - (item in B) for item in m))
