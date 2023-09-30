class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        ind1 = 0

        for item in s:
            cnt = t.count(item, ind1)
            if cnt == 0:
                return False
            else:
                ind1 = s.index(item, ind1)

        return True
    def isSubsequence1(self, s: str, t: str) -> bool:

        index = 0

        for item in t:

            if item == s[index]:
                index += 1

        return index == len(s)

    def isSubsequence2(self, s: str, t: str) -> bool:

        p1 = p2 = 0
        while p1 < len(s) and p2 < len(t):
            # move both pointers or just the right pointer
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        return p1 == len(s)



S1 = Solution()

print(S1.isSubsequence2(s = "axc", t = "ahbgdc"))
