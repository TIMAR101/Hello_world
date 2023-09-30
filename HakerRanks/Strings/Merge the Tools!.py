def merge_the_tools(string, k):

    ln = len(string)

    lnsub = ln//k

    for item in range(0, ln, k):
        res = ""

        for ch in range(item, item+k):

            if string[ch] in res:
                continue
            else:
                res += string[ch]

        print(res)

s = "AAABCADDE"
k = 3

merge_the_tools(s, k)


