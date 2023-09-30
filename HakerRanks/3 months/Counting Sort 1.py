def countingSort(arr):

    res = [0]*max(arr)

    for item in arr:

        res[item]+=1


    return res

print(countingSort([1,1,3,2,1]))



