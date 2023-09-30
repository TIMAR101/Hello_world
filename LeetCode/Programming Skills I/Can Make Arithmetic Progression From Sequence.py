class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:

        arr.sort()

        for item in range(0, len(arr)-2):

            if arr[item + 1] - arr[item] != arr[item+2] - arr[item+1]:
                return False

        return True

a = Solution()

print(a.canMakeArithmeticProgression([3,5,1]))
