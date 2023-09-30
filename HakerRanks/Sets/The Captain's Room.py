size = 5

ls = list(map(int, ("1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 ").split()))

print(ls)



setls = set(ls)

print(setls)

print((sum(setls)*5-sum(ls))//4)
