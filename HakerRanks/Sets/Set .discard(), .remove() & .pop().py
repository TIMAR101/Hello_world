n = int(input())

setn = set(map(int, input().split()))

m = int(input)

for _ in range(m):

    item = input()

    if "pop" in item:

        setn.pop()
    elif "remove" in item:

        item.replace("remove ", "")
        n = int(item)
        setn.remove(n)

    elif "discard" in item:

        item.replace("discard ", "")
        n = int(item)
        setn.discard(n)

print(setn)
        





