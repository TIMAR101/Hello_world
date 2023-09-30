import collections as cl

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        LenS = len(s)

        LenT = len(t)

        if LenS != LenT:
            return False

        ListS = []

        ListT = []

        for item in range(LenT):

            CountS = s.count(s[item], item)
            ListS.append(CountS)

            CountT = t.count(t[item],item)
            ListT.append(CountT)
            if CountT != CountS or s[item] == t[item]:
                return False

        return True

    def isIsomorphic1(self, s: str, t: str):

        if len(set(s)) != len(set(t)):
            return False

        hash_map = {}

        for char in range(len(t)):
            if t[char] not in hash_map:
                hash_map[t[char]] = s[char]
            elif hash_map[t[char]] != s[char]:
                return False

        return True

    def isIsomorphic3(self, s: str, t: str):

        pass

        #zipped_set = set(zip(s, t))
        #return len(zipped_set) == len(set(s)) == len(set(t))

    def isIsomorphic4(self, s, t):
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
        for idx in t:
            map2.append(t.index(idx))
        if map1 == map2:
            return True
        return False


S1 = Solution()

print(S1.isIsomorphic1(s = "bbbaaaba", t = "aaabbbba"))

s = "TImofey Ryabinin"
""""abc"
t =
"ahbgdc"""
s = "ahbgdc"

print(s.count("abc"))




















