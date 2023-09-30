import re

m = re.match("([abc])+", "abcc")
print(m)

m = re.match("(?:[abc])+", "bbbbb")
print(m)
