"""def fun(s):
    patten = "^[a-zA-Z0-9\-\_]+@[A-Za-z0-9]+[\.][a-zA-Z]{1,3}$"
    return re.search(patten,s)!=None

def fun(s):
  pattern = re.compile("^[\\w-]+@[0-9a-zA-Z]+\\.[a-z]{1,3}$")
  return pattern.match(s)

def fun(s):
    a = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s)
    return(a)

addr = re.compile(
    '''^
    [\w-]{1,}           #username
    @[a-zA-Z0-9]{1,}    #websitename
    \.\w{1,3}           #extension
    $''', re.UNICODE | re.VERBOSE)

import re
def fun(s):
    return bool(re.match(r"[A-Za-z0-9-_]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$", s))

def fun(s):
    m=re.fullmatch(r'[-\w]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}', s)
    return bool(m)

def fun(s):
    return bool(re.fullmatch('[A-Za-z0-9\-\_]+\@[A-Za-z0-9]+\.[A-Za-z]{2,3}', s))

def fun(s):
        import re
        return bool(re.match(r'^[\w-]+@[A-Za-z\d]+\.[a-zA-Z]{1,3}$', s))

def fun(s):
    return re.match(r"^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$", s) != None

import re

pattern=re.compile(r"^([a-zA-Z0-9_-])+@([a-zA-Z0-9])+\.([a-zA-Z]){1,3}$")

def fun(s):
    return re.match(pattern, s) != None

def fun(s):
    regex_pattern = r"^[a-zA-Z][a-zA-Z0-9-_]*[@][a-zA-Z0-9]+[.][a-zA-Z]{1,3}$"
    return re.match(regex_pattern, s)"""

import re
m = re.search('(?<=abc)def', 'abcdef')

print(type(m))
print(m)
print(m.string)
print(m.re)
print(m.pos)
print(m.group(0))

print(bool(re.fullmatch(r'(\w*)', "timofey")))

print(re.fullmatch(r'(\w*)', "timofey"))

print(bool(re.match(r'(\w)', "timofey")))




print(re.match(r'(\d*\w*)', "timofey123"))

print(re.findall(r'(\d*\w*)', "timofey123"))



"""re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
[('width', '20'), ('height', '10')]"""

print(r'/n\n\t\r')


p3 = re.compile(r"a[bcd]*b")

print(p3.match("abbbdddccdddccbd"))


p = re.compile(r'\bclass\b')
print(p.search(' #class at all'))

print(p.search('the declassified algorithm'))

print(p.search('one subclass is'))
