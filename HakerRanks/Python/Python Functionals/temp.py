l = list(range(10))
print(l)
l = list(map(lambda x:x*x, l))
print(l)

l = list(filter(lambda x: x > 10 and x < 80, l))

print(l)
