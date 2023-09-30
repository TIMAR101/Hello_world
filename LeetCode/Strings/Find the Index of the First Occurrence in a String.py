class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        return self.anotherSol(haystack, needle)

        lenHay = len(haystack)
        lenNeedle = len(needle)
        if lenNeedle > lenHay:
            return -1

        item1 = 0
        item2 = 0

        while item1 < lenHay:

            if haystack[item1] == needle[item2]:
                item2 += 1
                result = item1
                if item2 == lenNeedle:
                    return item1 - item2+1
            else:
                item2 = 0
                result = 0

            item1 += 1

        return - 1

    def SimpleSol(self, haystack: str, needle: str):

        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
    def anotherSol(self, haystack: str, needle: str):
        if len(needle) == 0:
            return 0
        elif needle not in haystack:
            return -1
        else:
            return len(haystack.split(needle)[0])




S1 = Solution()

print(S1.strStr(haystack = "mississippi", needle = "issip"))



haystack = "mississippi"

needle = "issip"
print(haystack.split(needle))

print(haystack.split("i"))




