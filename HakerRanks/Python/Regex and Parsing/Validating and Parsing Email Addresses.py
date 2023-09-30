# import email.utils
# print(email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>'))
# print(email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com')))

import re

#ptr = re.compile(r"$<[A-Za-z][A-z\-._]*@[A-Za-z]\.[A-Za-z]{1,3}>$")

ptr = re.compile(r"^<[A-Za-z][A-z\-._]*@[A-Za-z]+\.[A-Za-z]{1,3}>$")

# print(ptr.findall("<dexter@hotmail.com>"))


for __ in range(int(input())):

    name, mail = input().split()

    # print(name)
    # print(mail)
    if ptr.fullmatch(mail):

        print(name, mail)
