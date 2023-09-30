import collections as cl


class Solution:
    def removeElement(self, nums, val: int) -> int:

        return self.methodTwoPointers(nums, val)





    def methodTwoPointers(self, nums, val):

        lenNums = len(nums)

        slow = 0

        fast = 0


        for fast in range(0, lenNums):

            if nums[fast] == val:
                continue


            else:
                nums[slow] = nums[fast]
                slow += 1
        print(f"f = {fast}  s = {slow}")

        return nums

    def methodRemove(self, nums, val):




        while True:
            try:
                nums.remove(val)


            except:
                return len(nums)



    def methodNotTry(self, nums, val):

        nums = []

        while nums.count(val) != 0:

            ind = nums.index(val)
            nums.pop(ind)

        return len(nums)

    def removeElement1(self, nums, val):
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i

    def removeElement(self, nums, val):
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start +=1
    return start



S1 = Solution()

print(S1.removeElement(nums = [2], val = 3))

