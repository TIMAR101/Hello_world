if __name__ == '__main__':
    #n = int(input())
    #arr = map(int, input().split())

    arr = [2,3,6,6,5, 7, 4, 4, 10]

    arr.sort(reverse = True)

    for item in arr:

        if item < arr[0]:
            print(item)
            break

