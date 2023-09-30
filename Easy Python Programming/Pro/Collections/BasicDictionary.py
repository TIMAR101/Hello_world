UserDict={"Fname":"Timofey", "Sname": "Ryabinin", "Age":33}

print(UserDict)

MyMistress={
    "Natasha": 1,
    "Anna":2,
    "Inna":3
}
print(MyMistress)

print(f"lenf of UserDict: {len(UserDict)}")

print(f"lenf of MyMistress: {len(MyMistress)}")
print(type(MyMistress))

MyMistress1={
    1:"Natasha",
    2:"Anna",
    3:"Anna"
}
print(MyMistress1)

print("===================read=============================")
r=UserDict["Fname"]
print(r)
r=UserDict["Sname"]
print(r)
r=UserDict["Age"]
print(r)
print("===================get===============================")

r=UserDict.get("Age")
print(r)
print(UserDict.get("Fname"))
print("====================keys=====================")

print(UserDict.keys())
print(type(UserDict.keys()))

for item in UserDict.keys():
    print(f"keys = {item}")
    print(f"value= {UserDict[item]}")

print("=================value===================================")

print(UserDict.values())
print(type(UserDict.values()))

for item in UserDict.values():
    print(item)

for item in UserDict:
    print(item)
print(f"UserDict.items() = {UserDict.items()} type is {type(UserDict.items())}")
for key, val in UserDict.items():
    print(f"key = {key}")
    print(f"value = {val}")

print("=================================change==============================")
print(str(UserDict))
UserDict["Age"]=21
print(str(UserDict))

print("================================update")
print(MyMistress1)
MyMistress1.update({4: "Ksusha", 5: "Yana"})
print(MyMistress1)
MyMistress1.update(UserDict)
print(MyMistress1)

print("=====================================add=====================")
print(UserDict)
UserDict["Father Name"] = "Vladimir"
print(UserDict)
UserDict.update({"Cell":89097451625})
print(UserDict)

print("===================delete item=========================")
r=UserDict.pop("Cell")
print(r)
print(UserDict)
r=UserDict.popitem()
print(type(r))
print(r)
r=UserDict.popitem()
print(r)
print(UserDict)

del UserDict["Sname"]
print(UserDict)
del UserDict
print("--------------delll----------")
