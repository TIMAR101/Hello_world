class Solution:
    def twoSum(self, nums, target: int):

        dict1 = {}


        for i, num in enumerate(nums):
            reminder = target - num

            if num in dict1:
                return [dict1[num], i]

            else:
                dict1[reminder] = i




        """def finRes(num1, num2):

            nonlocal origList


            ind1 = origList.index(num1)
            if num1 == num2:
                ind2 = origList.index(num2, ind1+ 1)
            else:
                ind2 = origList.index(num2)

            return [ind1, ind2] if ind1 < ind2 else [ind2, ind1]


        LenList = len(nums)

        if LenList == 2:
            return [0, 1]


        origList = nums.copy()

        nums.sort()

        for i in range(0, LenList):

            for j in  nums:

                if origList[i] + j == target and i != origList.index(j):
                    return finRes(origList[i], j)
                elif origList[i] + j > target:
                    break"""









S1 = Solution()

print(S1.twoSum(nums = [5,75,25], target = 100))










        # for i in range(0, LenList):
        #
        #     for j in range(0, Len):
        #
        #         if nums[i] + nums[j] == target and i != j:
        #
        #             return [i, j]
