import math
#_________________________________________________________

r = input("Please enter the radius of the circle:   ")
r = float(r)
aoc = math.pi *r**2 #math.pow(r, 2)

print(f"The area of your circle is {aoc} with this radius {r}")
print("The area of your circle with the radious ({0}) is: {1} meters".format(r, aoc))
