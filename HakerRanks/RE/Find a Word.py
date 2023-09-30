

import re

data = 'foo bar (foo) bar foo-bar foo_bar foo"bar bar-foo bar, foo.'

patr = re.compile(r'\bfoo\b')

print(patr.findall(data))


