import re

p = re.compile(r'[^A-z\s]')
print(p.split('This is a test, short and sweet, of split().'))
