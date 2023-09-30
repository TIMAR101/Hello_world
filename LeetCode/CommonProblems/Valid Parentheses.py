class Solution:
    def isValid(self, s: str) -> bool:

        ListPar = ["(", ")", "[", "]", "{", "}"]

        OpenBraces = ["(", "[", "{"]

        CloseBraces = [")", "]", "}"]


        stec = []


        for item in s:

            if len(stec) == 0 and  item in OpenBraces:

                stec.append(item)
            elif len(stec) == 0 and item in CloseBraces:
                return False
            elif len(stec) != 0 and item in OpenBraces:
                stec.append(item)
            elif len(stec) != 0 and item in CloseBraces:
                sym = stec.pop()
                if item == "]" and sym == "[":
                    continue
                elif  item == "}" and sym == "{":
                    continue
                elif item == ')' and sym == "(":
                    continue
                else:
                    return False
        return True


S1=Solution()

print(S1.isValid("{[]}"))
