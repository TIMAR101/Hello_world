
MyList=["Yura", "Anton", "Serega", "Tema"]

print(MyList)
print(type(MyList))
MyList[0]="Yura1"
MyList[-1]="Tema1"

print(MyList)

print("======================append++++")

MyList.append("Maxim")
MyList.append("Misha")

print(MyList)

print("============================insert==========================")
MyList.insert(1, "Tolik")
MyList.insert(3, "Semen")
print(MyList)

print("-----------------------remove------------------------")
print(f"MyList.remove =    {MyList.remove('Tolik')} ")

print(f" pop(-1) = {MyList.pop(-1)}")





MyNumbers=[1,2,3,4,5,6,7,8,9,0]

print(MyNumbers)
MyNumbers.clear()
print(MyNumbers)

MyBools=[True, True, False, False]

print(MyBools)

MyMulti=[1, '1', True]
print(MyMulti)

print(len(MyNumbers))
print(len(MyBools))
#--------------------------read list------------------------------
print(MyMulti[0])
print(MyMulti[-1])








