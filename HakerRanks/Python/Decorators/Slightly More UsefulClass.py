class entryExit(object):

    def __init__(self, f):
        self.f = f

    def __call__(self, *b):
        print("Entering", self.f.__name__)
        
        self.f(*b)
        print("Exited", self.f.__name__)

@entryExit
def func1(a):
    print("inside func1()")
    print(f"a = {a}")

@entryExit
def func2():
    print("inside func2()")

func1(5)
func2()
