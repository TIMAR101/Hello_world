# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pt = re.compile(r".*?hackerrank.*?", re.I)

#data = "\n".join(input() for _ in range(int(input())))

data = "I love #hackerrank	I just scored 27 points in the Picking Cards challenge on #HackerRank	I just signed up for summer cup @hackerrank	interesting talk by hari, co-founder of hackerrank"

print(data)

print(pt.findall(data))

print(len(pt.findall(data)))

print(len(re.findall(re.compile(r"hackerrank", flags=re.I), '. '.join([input() for _ in range(int(input()))]))))

