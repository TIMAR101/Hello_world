

def longestCommonPrefix(strs) -> str:

        if len(strs) == 0 or len(strs[0]) == 0:
            return ''

        if len(strs) == 1:
            return strs[0]


        InitialString = strs[0]

        Flag = False
        Count = 0

        for i in InitialString:


            for s in strs[1:]:

                if (len(s) - 1) < Count:

                    return InitialString[0: Count]



                if InitialString[Count] != s[Count]:

                    return InitialString[0: Count]


            Count += 1

        return InitialString


print(longestCommonPrefix(["flower","flower","flower","flower"]))

round()




