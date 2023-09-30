MyAnimal=("Leva", "Musya", "Detusha", "Sema", "Filya")
MyNumbers=(1,2,3,4,5,6,7,8,9,0)
MyStaff=(True, "Leva", 1, False, "Musya", 2)
print("------------------joining Tuples-------------------------------")
MySumTuples=MyAnimal+MyNumbers
print(MySumTuples)


print("-----------------------------Multiply Tuples---------------------------------")
New_Tumple=MyAnimal*3
print(New_Tumple)
print("----------unpacking--------------------")

(n1, n2, n3, n4, n5)=MyAnimal
(m1, m2, m3, m4, m5,m6,)=MyStaff


print("------------------loop____________")

for item in MyAnimal:
    print(item)

print("---------------chekck if item exists")

if "Chernish" in MyAnimal:
    print("Please Timofey harry up to return Chernish!!!")
else:
    print("Please Timofey do it faster!!!")

if "Musya" in MyAnimal:
    print("Please Timofey harry up to return Musyu!!!")

print("------------------slising-------------------------")

Items=MyAnimal[-4:-2]
print(Items)
Items1=MyAnimal[1: 3]
print(Items1)
