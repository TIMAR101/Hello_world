class Solution:
    def removeDuplicates(self, nums) -> int:

        return self.methodTwoPointer(nums)




    def methodSet(self, nums):

        nums[:] = sorted(set(nums))
        return len(nums)

    def methodTwoPointer(self, nums):

        slow, fast = 0, 1
        while fast in range(len(nums)):
            if nums[slow] == nums[fast]:
                fast += 1

            else:
                nums[slow+1] = nums[fast]
                fast += 1
                slow += 1

        return slow + 1

    def methodPop(self, nums):
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

    def methodSet1(self, nums):
        numsset = set(nums)
        numsset = list(numsset)
        numsset.sort()
        # print(numsset)
        # print(nums)
        nums[:len(numsset)+1] = numsset[:]
        nums[:] = sorted(set(nums))
        return len(nums)


S1 = Solution()

S1.methodTwoPointer([0,0,1,1,1,2,2,3,3,4])




