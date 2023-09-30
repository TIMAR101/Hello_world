# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

pt = re.compile(r"^\([-+]?([1-8]?[0-9](\.[\d]+)?|90(\.0+)?),\s?[-+]?([1-9]?[0-9]?(\.[\d]+)?|1[0-7][0-9](\.[\d]+)?|180(\.0+)?)\)$")

# for _ in range(int(input())):
#
#     data = input()
#
#     if pt.fullmatch(data):
#         print("Valid")
#     else:
#         print("Invalid")



s1 = "(-90.0, -149.222)"

s2 = "(-20, -20)"

print(pt.fullmatch(s2))


