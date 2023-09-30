UserDict={"Fname":"Timofey", "Sname": "Ryabinin", "Age":33}

for k, v in UserDict.items():
    print(k,v)

for item in UserDict.values():
    print(f"values of the dictionary:  {item}")


for item in UserDict.keys():
    print(f"keys of the dictinary: {item}")
    print(f"values of the dictionary:  {UserDict[item]}")

Userdict1= UserDict.copy()
Userdict2=Userdict1
Userdict2["Age"]=20

Userdict2.clear()

print(Userdict1)
