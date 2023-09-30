import cmath

st = "-1+1j"



if "+" in st:
    pospl = st.index("+")
    a1 = int(st[0:pospl])
    a2 = int(st[pospl+1:-1])

else:
    pospl = st.index("-",1)
    a1 = int(st[0:pospl])
    a2 = int(st[pospl:-1])

print(a1)
print(a2)





"""1.41421356237
-0.785398163397
1-1j"""




p1 = cmath.phase(complex(a1, a2))

p2 = abs(complex(a1,a2))
print(p2)
print(p1)

