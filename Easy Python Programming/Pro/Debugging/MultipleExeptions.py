try:
    x=1
    y=1
    r=x/y
    print(r)
except ZeroDivisionError:
    print("Zero Division Error!!!")
except TypeError:
    print("Type Error!!!")
except:
    print("Other problems")
else:
    print("Else block")
finally:
    print("Finally block!!!")


print("It's great!!!")
