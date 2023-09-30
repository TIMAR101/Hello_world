class Coordinate(object):
     def __init__(self, x, y):
         self.x = x
         self.y = y
     def __repr__(self):
         return f"Coord: " + str(self.__dict__)
def add(a1, b1, t):

    print(locals())

    return  Coordinate(a1.x + b1.x, a1.y + b1.y)
def sub(a, b):
         return Coordinate(a.x - b.x, a.y - b.y)


def wrapper(func):

     print("def wrapper(func):")

     print(locals())
     def checker(a, b, t): # 1

         print("")

         print(locals())
         if a.x < 0 or a.y < 0:
             a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
         if b.x < 0 or b.y < 0:
             b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
         ret = func(a, b, "Rybinin")
         if ret.x < 0 or ret.y < 0:
             ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
         return ret
     return checker
one = Coordinate(100, 200)
two = Coordinate(300, 200)
three = Coordinate(-100, -100)
# print(sub(one, two))
#
# print(add(one, three))
# print("*"*100)
add = wrapper(add)
sub = wrapper(sub)
# print(sub(one, two))
#
# print(add(one, three))

add(one, two, "Timofey")


