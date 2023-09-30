import re

s1 = "i love hackerrank"
s2 = "hackerrank is an awesome place for programmers"
s3 = "hackerrank"
s4 = "i think hackerrank is a great place to hangout"

ptstart = re.compile(r'^hackerrank')

ptfinish = re.compile(r'.*hackerrank$')

print(ptstart.search(s4))

print(ptfinish.search(s4))


