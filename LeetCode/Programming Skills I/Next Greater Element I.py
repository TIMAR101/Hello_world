class Solution:
    def nextGreaterElement(self, nums1, nums2):

        output = []


        for item in nums1:
            ind = nums2.index(item)
            flag = False
            for item1 in nums2[ind+1:]:
                if item1 > item:
                    output.append(item1)
                    flag = True
                    break

            if not flag:
                output.append(-1)

        return output

S1 = Solution()

print(S1.nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))
