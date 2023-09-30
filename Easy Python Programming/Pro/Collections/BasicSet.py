MySet={"Cat", "Dog", "Goat"}

MySet1={1,2,3,4,5,6,7,8,9,0}
MySet2={True, False}

MySet3={"Cat", True, 809, 4145, (True, False)}

print(MySet1)
print(MySet2)
print(MySet3)
print(type(MySet3))

print(len(MySet3))

print("--------------------------read items--------------------------------------------------------------")

for item in MySet3:
    print(item)
print("-------------------------add items-------------------------------------------")

# add
MySet3.add("Dog")
MySet3.add("Goat")
print(MySet3)

# update

NewSet={"School", "University"}
NewTurple={"Pen", "Pencil"}
MySet3.update(NewSet)
print(MySet3)
MySet3.update(NewTurple)
print(MySet3)
MyList=["Mother", "Farther"]
MySet3.update(MyList)
print(MySet3)
MySet3.update(MySet1)
print(MySet3)
MySet2.update((1,2))
print(MySet2)

print(MySet3)

MySet3.discard(4145)
MySet3.discard(99999)
print(MySet3)
MySet3.remove("Pen")
print(MySet3)
print(MySet3.pop())
print(MySet3.clear())
