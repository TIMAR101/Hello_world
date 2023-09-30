# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

arr = input()
listarr = arr.split(sep=' ')

listnum = []

for item in range(len(listarr)):

    listnum.append(float(listarr[item]))

print(listnum)
Mean = sum(listnum)/ n
print(n)

if n % 2 == 0:

    Median = (listnum[n//2] + listnum[n//2-1]) / 2

else:
    n1 = n // 2
    Median = (listnum[n1-1] + listnum[n1+1]) / 2

DictMode = {}


for item in range(n):

    count = listnum.count(listnum[item])
    if count not in DictMode.keys():
        DictMode[count] = []
        DictMode[count].append(listnum[item])
    else:
        if listnum[item] not in DictMode[count]:
            DictMode[count].append(listnum[item])

print(DictMode)

maxModeKeys = max(DictMode.keys())

Mode = min(DictMode[maxModeKeys])

print(Mode)













