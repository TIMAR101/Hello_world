
def pivotIndex(nums):



        if sum(nums[1:]) == 0:
            return 0


        for item in range(0, len(nums)):

            RightSum = sum(nums[0:item])
            LeftSum = sum(nums[item+1:])

            if RightSum == LeftSum:
                return item

        return -1


l1 = [1,7,3,6,5,6]
print(sum(l1[0: 1]))

print(pivotIndex([1,7,3,6,5,6]))



