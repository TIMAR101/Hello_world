def MyFirstFunction(Fname, Number=1): #Parameter
    """This is my first function but with
    keyword arguments!!! Ok let's go!"""
    print(f"Hi my mistress {Fname}. Your number is {Number}")
    print("Another format: Hello my number {0} mistress {1}".format(Number, Fname))

MyFirstFunction(Fname="Natasha", Number=2)
MyFirstFunction(Number=3, Fname="Inna")
