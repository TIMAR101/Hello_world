# Advance try statement

try:
    x=1
    y=0+c
    r=x/y
    print(r)


except Exception as ex:
    print(type(ex))
    print(str(ex))


else:
    print("No Error!!!!")

finally:
    print("It's done!!!")

print("That's all")

