MyAnimal=("Leva", "Musya", "Detusha", "Sema", "Filya")
MyNumbers=(1,2,3,4,5,6,7,8,9,0)
MyStaff=(True, "Leva", 1, False, "Musya", 2)

print("-------------------read------------------------------")
Item=MyAnimal[1]
print(Item)
Item1=MyAnimal[-1]
print(Item1)

print(MyStaff)
print(type(MyStaff))
print(len(MyNumbers))

print(type(list(MyAnimal)))

print(type(tuple(MyAnimal)))
