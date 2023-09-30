import re

with open('Detect the Email Addresses', mode='r') as f:
    data = f.read()


ptr = re.compile(r"\b([\w.]+@[\w.]+\.[\w+]{1,3})\b")

#Emails = re.findall(r"[\w.]+@[\w.]+\.\w+",S)




print(*sorted(set(ptr.findall(data))), sep=";")

"""bd@tnmbonline.com;customerservice@tnmbonline.com;ibd@tnmbonline.com;nricell@tnmbonline.com;ttn_tmbankhi@sancharnet.in"""

"""hackers@hackerrank.com;interviewstreet@hackerrank.com;product@hackerrank.com"""
"""hackers@hackerrank.com;interviewstreet@hackerrank.com;product@hackerrank.com"""
