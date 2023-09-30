import sys

def camel(s):



    op1 = s[0]

    op2 = s[2]

    res = ""

    s = s[4:]

    if op1 == "S":

        res = s[0].lower()

        if s[-2:] == "()":

            s = s[:-2]

        for  item in s[1:]:



            if ord(item) < 97:


                res = res + " " + item.lower()

            else:
                res = res + item

    elif op1 == "C":



        ls = s.split(" ")

        if op2 == "V":

            res = ls[0][0].lower() + ls[0][1:]

            for item in ls[1:]:

                res = res + item[0].upper() + item[1:]

            return res
        elif op2 == "C":

            for item in ls:

                res = res + item[0].upper() + item[1:]
            return res

        elif op2 == "M":

            res = ls[0][0].lower() + ls[0][1:]

            for item in ls[1:]:

                res = res + item[0].upper() + item[1:]

            res = res + "()"

            return res










s= "S;C;OrangeHighlighter"

print(s)

print(camel(s))

# print(ord("a"))
#
# print(ord("z"))
#
# print(ord("Z"))
#
# print(ord("A"))
#
# print(ord(")"))
#
# s = "Timofey"
#
# s = s[2:-2]
#
# print(s)
