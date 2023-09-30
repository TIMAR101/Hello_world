import random as rd

def printTwoDimenson(TwoDim):

    for row in  TwoDim:

        for item in row:
            print(item, end=' / ')
        print()

temps = [[0.0 for h in range(24)] for d in range(31)]

print(len(temps))

print(len(temps[1]))

for item1 in range(len(temps)):

    print(len(temps))

    for item2 in range(len(temps[item1])):

        print(len(temps[item1]))

        temps[item1][item2]= rd.randint(-30, 50)


printTwoDimenson(temps)

max = - 40

min = 100

count=0

sum = 0

for n1 in temps:

    for n2 in n1:
        count +=1

        sum += n2

        if n2>max:
            max=n2

        if n2<min: min=n2



print(f"Max = {max}")

print(f"Average = {sum/count}")

print(f"Min = {min}")
