x = 1

while x <= 5:
    print(f"X = {x}")



    if x==3:
        break

    x= x + 1

else:

    print("X is not less than 5, any more!")


#-----------continue loop

x = 0

while x <= 5:
    x = x + 1

    if x==4 or x==6:
        continue

    print(f"The number is {x}")

