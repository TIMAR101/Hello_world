import re

ptr = re.compile(r"([A-z0-9])(\1)")

data = "__commit__"

print(ptr.search(data).groupdict())

print(ptr.findall(data))
