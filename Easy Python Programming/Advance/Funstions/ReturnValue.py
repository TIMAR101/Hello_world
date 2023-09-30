import datetime as dt

"""print(datetime.datetime.now())
print(type(datetime.datetime.now()))

dt = datetime.datetime.now()

print(dt.year)
print(type(dt.year))"""

year = dt.datetime.now().year
print(year)

def Age(YearofBirth=1990):
    """My first function with returning arguments"""
    return dt.datetime.now().year-YearofBirth


print(Age(1984))

print(Age(1990))
print((Age(1995)))
print(Age())
