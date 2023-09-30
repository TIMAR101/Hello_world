# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:

    if version < 4:
        return False
    else:
        return True


class Solution:
    def firstBadVersion(self, n: int) -> int:

        if n == 1:
            return 1

        left = 0
        right = n

        while left<=right:
            mid = (left+right)//2
            if isBadVersion(mid) == True and isBadVersion(mid - 1) == False:
                return mid
            elif isBadVersion(mid) == False:
                left = mid +1

            elif isBadVersion(mid) == True:
                right = mid-1


        return -1

    def firstBadVersion1(self, n):
        i = 1
        j = n
        while (i < j):
            pivot = (i+j) // 2
            if (isBadVersion(pivot)):
                j = pivot       # keep track of the leftmost bad version
            else:
                i = pivot + 1   # the one after the rightmost good version
        return i

     def firstBadVersion2(self, n: int) -> int:
        left = 1
        right = n
        result = 1

        while left<=right:
            mid = (left+right)//2
            if isBadVersion(mid) == False:
                left = mid+1
            else:
                right = mid-1
                result = mid

        return result



        """for item in range(n):

            if not(isBadVersion(n - item)):

                return n-item + 1

        return 1"""

S1 = Solution()

print(S1.firstBadVersion(5))
