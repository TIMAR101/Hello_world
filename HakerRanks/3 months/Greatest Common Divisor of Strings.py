class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if set(str1) != set(str2):
            return ""

        def comdiv(l1, l2):


            for item in range(l2+1, 0, -1):

                if l1 % item == 0 and l2 % item ==0:
                    return item



        ln1 = len(str1)

        ln2 = len(str2)

        comd = comdiv(ln1, ln2) if ln1 > ln2 else comdiv(ln2, ln1)

        if str1[0:comd] == str2[0:comd] and str1 == str1[0:comd] * (ln1//comd) and str2 == str2[0:comd] * (ln2//comd):
            return str1[0:comd]
        else:
            return ""

    def gcdOfStrings(self, str1, str2):
        s1, s2 = str1, str2
        while s2:
            s1, s2 = s2, s1[:len(s1)%len(s2)]

        if s1*(len(str1)//len(s1)) == str1 and s1*(len(str2)//len(s1)) == str2:
            return s1
        return ""

s1 = Solution()

print(s1.gcdOfStrings(str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX", str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))


def gcd(a: int, b: int) -> int:
            return b if a == 0 else gcd(b % a, a)

print(gcd(10,5))












