def one(*args1):
    print(type(args1))
    print(args1) # 1
one()

one(1, 2, 3)

def two(x, y, *args1): # 2
     print(x, y, args1)
two('a', 'b', 'c', "Timofey", "Lena")

l2 = [1,2,3,4,5,6,7,8,9]
two(*l2)


def add(x, y, z, *f):
     return x+y+z
lst = [1,2, 3, 4, 5]
print(add(lst[0], lst[1], lst[2])) # 1

print(add(*lst)) # 2

def foo(**kwargs):
     print( kwargs)
foo()

foo(x=1, y=2)


