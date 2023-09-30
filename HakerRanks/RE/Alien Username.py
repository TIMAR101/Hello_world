# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

pat = re.compile(r"^[_.][0-9]+[A-z]*_?$")



# for _ in range(int(input())):
#
#     data = input()
#
#     if pat.fullmatch(data):
#         print("VALID")
#     else:
#         print("INVALID")



pat = re.compile(r"^[._][0-9]+[A-Za-z]*_?$")

print(pat.fullmatch(".012341_anwqioerj_"))
