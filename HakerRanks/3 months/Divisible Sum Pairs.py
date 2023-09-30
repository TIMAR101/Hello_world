import itertools

def divisibleSumPairs(k, ar):

    res = 0

    for item in itertools.permutations(ar, 2):

        print(item)

        if sum(item) % k == 0:
            res+= 1

    return res//2

ar = [1, 3, 2, 6, 1, 2]

#ar = list(map(str, ar))

k = 3

print(divisibleSumPairs(k, ar))

#for item in itertools.



