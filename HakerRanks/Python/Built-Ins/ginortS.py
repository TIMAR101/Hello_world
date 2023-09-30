print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')

print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='')

import string
print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')


print(*(sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))), sep='')

def getKey(x):
    if x.islower():
        return(1,x)
    elif x.isupper():
        return(2,x)
    elif x.isdigit() :
        if int(x)%2==1:
            return(3,x)
        else :
            return(4,x)

print(*sorted(input(),key=getKey),sep='')

s = input()
s = sorted(s,key = lambda x:(x.isdigit() and int(x)%2==0, x.isdigit(),x.isupper(),x.islower(),x))
print(*(s),sep = '')

S = input()
low = sorted([a for a in S if a.islower()])
up = sorted([a for a in S if a.isupper()])
odd = sorted([a for a in S if a in ["1","3","5","7","9"]])
even = sorted([a for a in S if a in ["0","2","4","6","8"]])

print("".join(low+up+odd+even))

import re
s = input()
l = sorted(re.findall('[a-z]', s)) + sorted(re.findall('[A-Z]', s)) + sorted(re.findall('[13579]', s)) + sorted(re.findall('[24680]', s))
print(''.join(l))

def sort_key(c):
    return (
    c in ('0', '2', '4', '6', '8'), c.isdigit(), c.isupper(), c
    )

print(*sorted(input(), key=sort_key), sep='')
