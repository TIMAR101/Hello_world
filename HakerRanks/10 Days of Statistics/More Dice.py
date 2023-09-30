import fractions

one = [1, 2, 3, 4, 5, 6]
two = [1, 2, 3, 4, 5, 6]
three = []
four = []

for i in one:
    for j in two:
        if i != j and i + j == 6:
            three.append((i, j))
        if i + j > 9:
            four.append((i, j))

count = len(three)
total = len(one) * len(two)
prob = fractions.Fraction(count, total)

print(type(prob))

print(prob)

prob = fractions.Fraction(len(four), total)
print(prob)

