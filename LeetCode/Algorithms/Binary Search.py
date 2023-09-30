class Solution:





    def search(self, nums, target: int) -> int:

        left = 0
;
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1

        return -1

C1 = Solution()

C1.search([1,2,3,4,5,6,7,8,9,10], 7)






