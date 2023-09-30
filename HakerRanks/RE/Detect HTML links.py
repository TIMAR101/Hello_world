

import re

link = re.compile(r'<a href="([^"]+)"[^/]*>([^<]*)<')

pattern = re.compile(r"<a\shref=\"(.+?)\".*?(?<=>)([^><]*?)(?=<\/)")

data1='<a href="http://www.hackerrank.com"><h1><b>HackerRank</b></h1></a>'

data2 = '<div class="more-info"><a href="http://www./examples/html_links_examples.cfm">More Link Examples...</a></div>'
# m = re.search('(?<=abc)def', 'abcdef')
ptrlink = re.compile(r'(?<=<a href=\").+?(?=")')

ptrname = re.compile(r'(?<=>)[\w\s .,/]+?(?=<)')

ptrcommon = re.compile(r'(?<=href=\")(.+?)(?=")(?:.*?)(?<=>)[\w .,]+?(?=<)')

print(link.findall(data1))
print(link.findall(data2))

# print(ptrlink.findall(data1))
# print(ptrname.findall(data1))

# for item in ptrlink.finditer(data2):
#
#     print(item.group(), ",", end="", sep="")
#     pos = item.start()
#     if ptrname.search(data1, pos=pos):
#         print(ptrname.search(data2, pos=pos).group())

# pos = ptrlink.search(data1).start()
# print(ptrname.search(data1, pos=pos))
# print(ptrname.findall(data1))
#
# print(ptrlink.search(data2))
# print(ptrname.findall(data2))

#print(f"{ptrlink.search(data2).group()},{ptrname.search(data2).group()}")


# for _ in range(int(input())):
#
#     data = input()
#
#     if ptrlink.search(data):
#
#         for item in ptrlink.finditer(data):
#
#             print(item.group(), ",", end="", sep="")
#             pos = item.start()
#
#             if ptrname.search(data, pos=pos):
#                 print(ptrname.search(data, pos=pos).group().strip(), end="", sep="")
#
#             print()


