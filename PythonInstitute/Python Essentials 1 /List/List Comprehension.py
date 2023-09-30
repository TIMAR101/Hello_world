row = ["WHITE_PAWN" for i in range(8)]

print(type(row))
print(row)

squares = [x ** 2 for x in range(10)]

print(squares)

twos = [2 ** i for i in range(8)]

odds = [x for x in squares if x % 2 != 0 ]

print(odds)

simple = [x for x in squares if x % 2 == 0 ]

print(simple)
