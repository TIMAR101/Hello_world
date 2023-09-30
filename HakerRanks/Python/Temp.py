# d = []
#
# commands = {
#     'append': lambda x: d.append(x),
#     'pop': lambda : d.pop(),
#     'appendleft': lambda x: d.appendleft(x),
#     'popleft': lambda : d.popleft()
# }
#
# print(commands)
#
# print(type(commands["append"]))
#
# comm = "pop"
#
# operation = commands.get(comm, lambda : None)
#
# operation1 = commands.get(comm)
#
# print(operation)
#
# print(operation1)
#
#
#
# b = [1,2,3]
#
# a = []
#
# func = getattr(a, "append")
#
# l = getattr(a, "__len__")
#
# c = getattr(b, "clear")
#
# print(func)
#
# func(1)
# print(a)
#
# print(l)
#
# print(l)
#
# print(c)
# print(b)
# c()
#
# print(b)
#
# a= "1"
#
# b=2
#
# print(eval(f"{int(a)}+{b}"))
#
# eval(f"print({int(a)}+{b})")
#
#
# a = []
#
#
# eval(f"a.append(5)")
#
# eval("print(a)")
#
#
#
# #eval('d.{}({})'.format(name,str(*no)))
#
# import collections
#
# from collections import deque
#
# d1 = deque()
#
# funs1 = {'append': deque.append, 'pop': deque.pop, 'popleft': deque.popleft, 'appendleft': deque.appendleft}
#
# print(funs1["append"])
#
# a = funs1["append"]
#
# a(d1,5)
#
# print(a)
# print(d1)
#

print(print(2+3))

"""list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]"""

ls = list(range(3, 6))
print(ls)

ls1 = list(range(*ls))
print(ls1)

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
print(*d)

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

parrot(**d)

import string

print(string.ascii_letters)

print(string.hexdigits)


print(type(string.ascii_letters))


print(string.ascii_letters.index("c"))

def sort_key(c):
    return (
    c in ('0', '2', '4', '6', '8'), c.isdigit(), c.isupper(), c
    )

print(sort_key("2"))

print(type(sort_key("")))

lm = lambda x:(x.isdigit() and int(x)%2==0, x.isdigit(),x.isupper(),x.islower(),x)

print(lm("5"))

print(sorted("Timofey$R123456#", key= lambda c:(c.isdigit() and int(c)%2==0, c.islower())))

print(sorted("Timofey$R123456#", key= lambda c:(c.isdigit() and int(c)%2==0, c.islower(), c)))

print(list(range(2,3)))
