def diagonalDifference(arr):

    d1 = 0

    d2 = 0

    ln = len(arr)


    for item in range(ln):

        d1 += arr[item][item]

        d2 +=arr[item][ln-item-1]

    return abs(d1-d2)

def diagonalDifference1(arr):

    return abs(sum(arr[item][item] - arr[item][len(arr)-item-1] for item in range(len(arr))))

print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))

print(diagonalDifference1([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))


