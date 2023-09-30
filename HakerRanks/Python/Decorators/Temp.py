def outer():
    print("inside outer")
    def inner():
        print("Inside inner")

    print(locals())
    return inner # 1

foo = outer() #2


foo()

print(foo.__name__)

print(foo.__class__)
print(foo.__closure__)
