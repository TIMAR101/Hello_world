import platform

r = platform.uname()


print(f"platrom.unatme result type is {type(r)}. The result is {r}")

r = platform.machine()

r1 = type(r)
print("type is platform.machine is {0}. The result is {1}.".format(r1, r))
