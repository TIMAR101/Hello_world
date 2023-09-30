x = 7
y = 8
z = 9
n = 10


print([[a, b, c] for a in range(x + 1) for b in range(y + 1) for
       c in range(z + 1) if (a+b+c != n)])
f= 1
squares = [x ** 2 for x in range(10)]
List1 = [[l, g] for l in range(4) for g in range(4) if l < 2 and g > 2]
print(List1)

List1.sort()

odds = [x for x in squares if x % 2 != 0 ] # The snippet makes a list with only the odd elements of the squares list.
