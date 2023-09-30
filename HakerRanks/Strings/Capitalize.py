def solve(s):

    slist = s.split()

    res = []

    for item in slist:
        item = item.capitalize()

        res.append(item)

    st = " ".join(res)

    st = st.strip()



    return st




print(solve("hello   world  lol"))


