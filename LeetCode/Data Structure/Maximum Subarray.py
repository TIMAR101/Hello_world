
def maxSubArray(nums) -> int:

        if len(nums) == 1:
            return nums[0]


        MaxSum = max(nums)

        MinSum = min(nums)





        for item1 in range(len(nums)):

            Sum = 0

            for item2 in range(item1+1, len(nums)+1):

                Sum = sum(nums[item1: item2])

                if MaxSum < Sum:

                    MaxSum = Sum

        return MaxSum


print(maxSubArray([-2,-1]))

list = []



print(int(2.5))

print(5//2)
