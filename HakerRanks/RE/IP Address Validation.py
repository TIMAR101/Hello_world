import re

pt4 = re.compile(r"^[\d]?[\d]{,2}(\.[\d]?[\d]{,2}){3}$")

pt6 = re.compile(r"^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7}$")

print(pt4.match("255.255.255.8"))
print(pt6.match("1050:1000:1000:a000:5:600:300c:326b"))
