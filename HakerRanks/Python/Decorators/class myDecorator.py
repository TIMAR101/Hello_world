class myDecorator(object):

    def __init__(self, f):
        print("inside myDecorator.__init__()")
        f() # Prove that function definition has completed

    def __call__(self):
        print("inside myDecorator.__call__()")
        

@myDecorator
def aFunction():
    print("inside aFunction()")

print( "Finished decorating aFunction()")

aFunction()
#
# aFunction()
# aFunction()
