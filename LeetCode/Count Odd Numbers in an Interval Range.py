
def countOdds(low: int, high: int) -> int:

        if low < 0 or high > 10**9 or low > high:
            return 0

        count = 0

        for i in range(low, high+1):

            if i % 2 != 0:
                count +=1


        return count

def countOdds1(low: int, high: int) -> int:

    if low % 2 != 0 and high % 2 ==0:
        return int(high - low + 1) / 2

    if low % 2 == 0 and high % 2 == 0:
        return int(high - low) / 2

    if low % 2 == 0 and high % 2 !=0:
        return int(high - low + 1) / 2

    if low % 2 != 0 and high % 2 !=0:
        return int(high - low + 2) / 2




# print(countOdds(1,10))  # 9 --- 5  9+1/2   10-1-1/2 + 1
# print(countOdds(3, 14)) # 11 --- 6     11+1/2
#
# print(countOdds(7, 14)) #  7+1/2 =4

print(countOdds(2, 8)) # 6 -----3

print(countOdds(8, 16))
print(countOdds(4, 11)) # 7--------4
print(countOdds(7, 17))  #11+1

print(countOdds(5, 13))








