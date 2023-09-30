s = set("Hacker")

print(s)

s=s.union("Rank")

print(s)
s = s.union(enumerate(["R", "a", "n", "k"]))
print(s)

s = s.union({[1,2]})
print(s)
