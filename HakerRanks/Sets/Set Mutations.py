# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

nset = set(map(int, input().split()))

b = int(input())

for __ in range(b):

    item = input()

    if "intersection_update" in item:

        item = item.replace("intersection_update ", '')

        bset = set(map(int, item.split()))

        nset.intersection_update(bset)

    elif "symmetric_difference_update" in item:

        item = item.replace("symmetric_difference_update ", '')

        bset = set(map(int, item.split()))

        nset.symmetric_difference_update(bset)

    elif "difference_update" in item:

        item = item.replace("difference_update ", '')

        bset = set(map(int, item.split()))

        nset.difference_update(bset)

    elif "update" in item:

        item = item.replace("update ", '')

        bset = set(map(int, item.split()))

        nset.update(bset)

    print(nset)


print(sum(nset))
