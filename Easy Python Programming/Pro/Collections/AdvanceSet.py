S1={0,1,2,3,4,5}
S2={4,5,6,7,8,9}

print("--------------union----------------------------")

UnionSet=S1.union(S2)

print(UnionSet)

print("================intersection==============================")

InterSet=S1.intersection(S2)
print(InterSet)

print("===================difference=========================")

DifSet=S1.difference(S2)

print(DifSet)

Difset1=S2.difference(S1)
print(Difset1)

print("================symetric dirrerences---------------------------")

SimSet1=S1.symmetric_difference(S2)

SimSet2=S2.symmetric_difference(S1)

print(f"S1.symmetric_difference(S2) = {SimSet1}")

print(f"S2.symmetric_difference(S1) = {SimSet2}")
