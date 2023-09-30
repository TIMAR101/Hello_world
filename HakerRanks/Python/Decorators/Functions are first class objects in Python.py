def outer():
     def inner():
         print("Inside inner")
     return inner # 1

foo = outer() #2


print(foo)
print(type(foo))

foo.__name__ = "Timofey"

print(foo)

print(foo.__name__)

print(foo.__closure__)
print(foo.__class__)

print(foo())
