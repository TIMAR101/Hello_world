import re

p = re.compile(r'(?P<word>\b\w+\b)\s(?P=word)')
m = p.search( '(((( Lots of of punctuation )))' )
print(m.group('word'))
#
print(m.group(1))
print(m.group())

print(p.findall('(((( Lots of of punctuation )))'))
