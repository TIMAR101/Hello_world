class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        lens1 = len(s1)
        lens2 = len(s2)


        if lens1 != lens2:
            return False
        if sorted(s1) != sorted(s2):
            return False

        count = 0
        sets1 = set()
        sets2 = set()

        for item in range(len(s1)):

            if s1[item] != s2[item]:
                count += 1
                if count > 3:
                    return False
                sets1.add(s1[item])

                sets2.add(s2[item])

        return sets1 == sets2

sol = Solution()

sol.areAlmostEqual("syvse", "yvsse")



