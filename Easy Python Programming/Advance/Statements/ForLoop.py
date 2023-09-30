a="Hello Python! I hope you will rescue me"

for x in a:
    print(x)
    if x=="h" or x == "H":
        break

else:
    print("It's done!")
    print("Python will release me!!!")

#========================================================================

MyList=[1, 2, 3, 4, 5, 6, 7, 8]
MyList1 = ["Timofey", "Irina", "Aliya", "Natasha"]
print(MyList)
print(MyList1)


#=======================
for FirstName in MyList1:

    if FirstName=="Natasha":
        break
    print(FirstName)
else:
    print("It's done")
#----------continue--------------
a="Hello Python! I hope you will rescue me"

for x in a:

    if x=="h" or x == "H":
        continue
    print(x)

else:
    print("It's done!")
    print("Python will release me!!!")
#----pass----

MyList=[1, 2, 3, 4, 5, 6, 7, 8]

for x in MyList:
    pass
