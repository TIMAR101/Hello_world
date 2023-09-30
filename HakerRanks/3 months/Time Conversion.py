def timeConversion(s):
    # Write your code here

    if "AM" in s:

        return s[:-2]

    else:

        print(s[0:3])

        h = int(s[0:2])

        if h == 12:

            hs = "00"

        else:
            hs = str(h+12)

        return hs + s[2:-2]

print(timeConversion("07:05:45PM"))
