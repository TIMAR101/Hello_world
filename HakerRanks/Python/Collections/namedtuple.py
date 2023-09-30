

import collections
Point = collections.namedtuple("Point", "x,y")

print(Point)
print(type(Point))
pt1 = Point(1,2)

pt2 = Point(3,4)

print(pt1, pt2)

dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )

print(dot_product)

Car = collections.namedtuple('Car','Price Mileage Colour Class')
xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')

print(xyz)

print(xyz.Price)

print(xyz.count(70))

print("+"*100)

Person = collections.namedtuple("Person", "Firstname Lastname")

Timofey = Person("Timofey", "Ryabinin")
print(Timofey)


print(Timofey.Firstname)

Irina = Person("Irina", "Ryabinina")
print(Irina.Lastname)

a, b = Irina
print(a)
print(b)
ls = ["Maksim", "Ryabinin"]
Maksim = Person._make(ls)

print(Maksim)

Maksim._make(ls)

print(Maksim)
print(Maksim.Firstname)


column_names = ["ID", "MARKS", "NAME", "CLASS" ]

column_names.
mark_index = column_names.index('MARKS')
sum_marks = 0
for i in range(N):
    mark = input().split()[mark_index]
    sum_marks += int(mark)

print(round(sum_marks/N, 2))



