def foo(**kw):
     print(kw)

def foo1(*kw):
     print(kw)

def foo2(*kw, **kw1):
     print(kw)
     print(kw1)
foo()

foo2(x=1, y=2)

foo2(x=1, y=2, z=3)

foo2(x = [1,2,3])

dc = {"c":3, 'd':5}

foo2(**dc)

foo2(*dc)
