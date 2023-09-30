# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

llist = []

for item in range(n):
    st = input()
    llist.append(st)


for item in llist:
    evenlist = []
    notevenlist = []

    for sym in range(len(item)):



        if sym % 2 == 0:
            evenlist.append(item[sym])

        else:
            notevenlist.append(item[sym])

    evenstring = ''.join(evenlist)
    notevenstring = ''.join(notevenlist)
    print(evenstring, " ", notevenstring)



