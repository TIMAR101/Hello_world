from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:

        sets = set(s)


        flagone = False
        flagnech = False
        polLen = 0
        maxcountnch = 3

        for item in sets:

            count = s.count(item)

            if count % 2 != 0:
                if flagnech == False:
                    polLen += count
                    flagnech = True
                elif count > 1:
                    polLen = polLen + count - 1
                else:
                    continue
            else:
                polLen+= count

        return polLen
    def longestPalindrome1(self, s: str) -> int:

        c = Counter(s)
        sum = 0
        for item in c.values():

            sum = sum + (item // 2) *2

        return sum + 1 if sum != len(s) else sum


S1 = Solution()

print(S1.longestPalindrome(s = "bananas"))
print(S1.longestPalindrome1(s = "bananas")) # "bananas" bans 7 - 4 = 3

c = Counter('gallahad')
print(c)


