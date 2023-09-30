import re

m = re.match("([abc])+", "abc")
print(m.groups())


#m = re.match("(?:[abc])+\w", "abct")

m = re.search(r"(?<=<)\w(?=>)", "<a>")
print(m.group())

m = re.search(r"(?:[<\s*])[A-z]*", "<a>")
print(m.group())
