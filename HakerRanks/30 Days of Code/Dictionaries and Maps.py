# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n = int(input())

dictphone = {}

for item in range (n):
    
    phoneList = input().strip().split(sep=' ')
    dictphone.update({phoneList[0]:phoneList[1]})
quar = input()   
quarList = []
# while quar != '':
#
#     quarList.append(quar)
#     quar = input()

lines = sys.stdin.readlines()

print(lines)
print(type(lines))
    
for item in quarList:
    
    phone = dictphone.get(item)
    if phone != None:
        print(f"{item}={phone}")
    else:
        print("Not found")
    
    
    
