import re

ptr = re.compile(r"(?:https?://www.|https?://ww2.|https?://)([^/\"\)\s\+]+\.\w{3})")

ptr = re.compile(r"(?:https?://www.|https?://ww2.|https?://)([\w\.-]+)")

ptr = re.compile(r"(?:https?://www.|https?://ww2.|https?://)([\w.\-]*\.[\w\-]+[^_\W])")

# r'(?<=://)[\w\d-]+[\.]+[\w\.-]+'



with open('Detect the Domain Name', mode='r') as f:
    data = f.read()

# data1 = 'http://www.xyz.com/news, https://abc.xyz.com/jobs, http://abcd.xyz.com/jobs2'
#
# data2 = ""

setl = set()

for item in ptr.finditer(data):

     print(item)
     print(item.group(0))
     # print(item.group())

     setl.add(item.group(0))

print(*sorted(setl), sep=";")

#askoxford.com;bnsf.com;hydrogencarsnow.com;mrvc.indianrail.gov.in;web.archive.org




#print(*sorted(set(ptr.findall(data1).group(1))), sep=";")

#  [xyz.com, abc.xyz.com, abcd.xyz.com]

