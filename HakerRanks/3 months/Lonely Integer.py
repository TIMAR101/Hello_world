import collections


def lonelyinteger(a):

    c = collections.Counter(a)

    for item in c.items():

        print(item)

        if item[1]==1:
            return item[0]


def lonelyinteger1(a):

    map = {}

    for item in a:

        map[item] = map.get(item) + 1

    print(map)

    for item in map:

        if item[1]==1:
            return item[0]



#print(lonelyinteger1([1,1,2,2,3]))

a = {1:2,}

a.setdefault(3,-1)



print(a.get(4))


