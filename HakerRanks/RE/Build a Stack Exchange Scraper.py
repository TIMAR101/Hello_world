

#Build a Stack Exchange Scraper.txt

#  f = open('workfile', 'w', encoding="utf-8")

"""with open('output.txt', 'w') as f:
    f.write('Hi there!')"""
# <h3><a href="/questions/

"""
80407;about power supply of operational amplifier;11 hours ago
80405;5V Regulator Power Dissipation;11 hours ago
"""
"""
import re
import sys
S = sys.stdin.read()

question = r"(?<=questions/)\d+"
title = r"(?<=question-hyperlink\">).+(?=</a>)"
time = r"(?<=relativetime\">).+(?=</span>)"

for i in list(zip(re.findall(question,S),re.findall(title,S),re.findall(time,S))):
    print(*i,sep=";")"""

import re
ptN = re.compile(r'(?<=<h3><a href="/questions/)(\d+)')


ptQ = re.compile(r'(?<=question-hyperlink">)(.+)(?=</a>)')

ptT = re.compile(r'(?<=class="relativetime">)(.+)(?=</span>)')   #</span>



with open("Build a Stack Exchange Scraper1.txt", "tr+") as f:

    data = f.read()

print(ptN.findall(data))

print(ptQ.findall(data))


print(ptT.findall(data))


lsN = ptN.findall(data)

lsQ = ptQ.findall(data)

lsT = ptT.findall(data)
print("*"*100)
for i in zip(lsN, lsQ,lsT):
    print(i)
    print(*i)
    print(list(i))

print("*"*100)



#print(lsN)

#print(lsQ)

#print(lsT)



for n in range(len(lsN)): o;
,,,,,,,,,,,,,,,,,,,,,,,,,,;;;;;;;;;;;;;
    print(f"{lsN[n]};{lsQ[n]};{lsT[n]}")















