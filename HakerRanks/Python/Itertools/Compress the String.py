
import itertools

s = "111222333444567"

# print([k for k, g in itertools.groupby('AAAABBBCCDAABBB')])
# print([list(g) for k, g in itertools.groupby('AAAABBBCCD')])
#
# print([item for item in itertools.groupby('AAAABBBCCDAABBB')])

for item in itertools.groupby("1222311"):

    #print(len(tuple(item[1])))

    #print(item[0])
    #print(len(tuple(item[1])))
    print(f"({len(tuple(item[1]))}, {item[0]})", end=" ")

# (1, 1) (3, 2) (1, 3) (2, 1)item[0]
