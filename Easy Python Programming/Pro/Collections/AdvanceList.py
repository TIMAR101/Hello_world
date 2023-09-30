MyGirls=["Luda", "Darya", "Natasha", "Anna", "Inna", "Kshuha"]

print("===============copy======================================")

MyNewGirl=MyGirls.copy()

MyNewGirl1=list(MyGirls)



print("----------------------reversing-------------------------")
print(MyGirls)
MyGirls.reverse()

print(MyGirls)
MyGirls.reverse()
print(MyGirls)

#----------------slicing--------------------
r=MyGirls[:2]
print(type(r))
print(r)

r=MyGirls[-2:]
print(r)

print(MyGirls[2:4])
print(MyGirls[-4:-2])

print("------------------check if exists----------------------")

rr= "Albina" in MyGirls
print(rr)
rr = "Natasha" in MyGirls
print(rr)

print("--------------------------loop in list---------------")
for item in MyGirls:
    print(item)

print("--------------------------------sort list------------------")

print(MyGirls)
MyGirls.sort()
print(MyGirls)
MyGirls.sort(reverse=True)
print(MyGirls)

print("="*100, sep="Extend")

MyGirls.extend(MyNewGirl)
print(MyGirls)
MyNumber=[1,2,3,4,5,6,7,8,9,0]
MyNumber.extend(MyNumber)
print(MyNumber)

print("============================join==========================")

New_List=MyGirls+MyNumber
print(New_List)

for item in MyGirls:

    MyNumber.append(item)

print(MyNumber)

