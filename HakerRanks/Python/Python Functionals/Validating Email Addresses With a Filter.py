import string

def fun(s):
    # return True if s is a valid email, else return False


    ind1 = s.find("@")

    if ind1 == -1 or ind1 == 0:
        return False
    else:

        inter1 = string.ascii_letters + string.digits + "-_"


        for item in s[:ind1]:

            if not item in inter1:
                return False

    ind2 = s.find(".",ind1)

    if ind2 == -1:
        return False
    else:
        inter2 = string.ascii_letters + string.digits

        for item in s[ind1+1:ind2]:
            if not item in inter2:
                return False

    if len(s[ind2+1:]) > 3:
        return False
    else:
        for item in s[ind2+1:]:
            if not item in string.ascii_letters:
                return False

    return True

import re
def fun(s):
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
    return re.match(regex_pattern, s)

print(sorted(filter(addr.search, (input() for _ in range(int(input()))))))

def check_valid(email):
    try:
        username, url = email.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False

    if username.replace("-", "").replace("_", "").isalnum() is False:
        return False
    elif website.isalnum() is False:
        return False
    elif len(extension) > 3:
        return False
    else:
        return True

"""\w              => matches alphabets and numbers including 
underscore
-               => matches -
[\w-]           => will match either of them
[\w-]+          => means once or more than once

@               => match @
[0-9|a-z|A-Z]+  => match the given range of alphabets and numbers one or more than once
\.              => will match character .
[a-z]{1, 3}     => will match any string that has lowercase and 
length one, two or three"""


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
