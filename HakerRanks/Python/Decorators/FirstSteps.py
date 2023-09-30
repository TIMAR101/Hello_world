# a_string = "This is a global variable"
# def foo(x):
#     c = 5
#
#     d = "Timofey"
#
#     print(locals())
# print(globals()) # doctest: +ELLIPSIS
#
# foo(5) # 2

# print(issubclass(int, object)) # all objects in Python inherit from a common baseclass
#
# def foo():
#     pass
# print(foo.__class__)
#
# print(issubclass(foo.__class__, object))

# def outer():
#      xouter = 1
#
#      def inner():
#          print("Inside inner")
#          xinner = 1
#          print(xouter)
#          print(locals())
#      return inner # 1
#
# foo = outer() #2
# print(foo) # doctest:+ELLIPSIS
# print(type(foo))
#
# foo()
#
# print(foo.__closure__)
#
# print(foo.__class__)
#
# print(foo.__builtins__)
#
# print(foo.__globals__)
#
# print(foo.__sizeof__())


def outer(x):
     def inner():
         print(x) # 1
         print(locals())
     return inner
print1 = outer(1)
print2 = outer(2)
print1()

print2()



