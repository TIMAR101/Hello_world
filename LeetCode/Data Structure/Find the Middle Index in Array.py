class Solution:
    def findMiddleIndex(self, nums) -> int:

        if len(nums) <=1:
            return -1

        ArrSum = sum(nums)

        ArrSumLeft = 0
        ArrSumRight = ArrSum - nums[0]
        if ArrSumRight == 0:
            return 0

        for item in range(1, len(nums)):
            ArrSumLeft +=nums[item-1]
            ArrSumRight  = ArrSumRight - nums[item]
            if ArrSumRight == ArrSumLeft:
                return item
        return -1

class Solution1:
    def findMiddleIndex(self, nums) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1

class Solution2:
    def findMiddleIndex(self, nums) -> int:
        left = 0 # nums[0] + nums[1] + ... + nums[middleIndex-1]
        right = sum(nums) # nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1]

        for i, num in enumerate(nums): # we can use normal for loop as well.
            right -= num # as we are trying to find out middle index so iteratively we`ll reduce the value of right to find the middle index
            if left == right: # comparing the values for finding out the middle index.
                return i # if there is any return the index whixh will be our required index.
            left += num # we have to add the num iteratively.

        return -1

class Solution3:
    def findMiddleIndex(self, nums) -> int:
        A = [0] + list(accumulate(nums)) + [0]
        total, n = sum(nums), len(nums)
        for i in range(n):
            if A[i] == total - A[i] - nums[i]:
                return i
        return -1

S1 = Solution()

print(S1.findMiddleIndex([5]))

print(enumerate(range(5)))

T1 = enumerate(range(5))
print(type(T1))

for e1, e2 in enumerate(range(5), start=100):

    print(e1, end=" ")
    print(e2)

for e in enumerate(range(5), start=777):

    print(e)









