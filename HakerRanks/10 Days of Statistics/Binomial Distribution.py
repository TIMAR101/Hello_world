# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

boys, girls = map(float, input().split())
p_boys = boys/(boys + girls)
p_girls = 1 - p_boys
b = []
n_children = 6
n_boys = 3
for i in range(n_boys, n_children+1):
    answer = math.comb(6, i) * (p_boys ** i) * (p_girls ** (n_children - i))
    b.append(answer)

print(round(sum(b), 3))


import math
x,y=map(float,input().split())
p=x/(y+x)
q=1-p
b=[]
for i in range(3,6+1):
    f=math.comb(6,i)*(p**i)*(q**(6-i))
    b.append(f)
print(round((sum(b)),3))
