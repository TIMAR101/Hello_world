def outer(some_func):

     def inner(xinn):

         print("def inner(x):")

         print(locals())
         print("before some_func")
         ret = some_func(xinn+1) # 1
         print("def inner(x):22")
         print(locals())
         return ret + 1
     print("def outer(some_func):")
     print(locals())
     return inner
def foo(x):
    y = 1
    print("def foo(x):")
    print(locals())
    return x + y
decorated = outer(foo) # 2

print(decorated(3))
