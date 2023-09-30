try:
    print(x)
except NameError:
    print("Name Error!!!")
finally:
    print("It's have done")

#-----------------------------------
print("---"*100)
try:
    x=1
    y=0
    r=x/y
    print(r)
except ZeroDivisionError:
    print("Division by zero is not valid!!!")
finally:
    print("It's done")

print("Hi!!!")










