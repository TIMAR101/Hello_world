# Enter your code here. Read input from STDIN. Print output to STDOUT

import re


# ptrtag = re.compile(r'(?<=<)\w+(?=\s)')

ptrtagv1 = re.compile(r'(?<=<)(\w+)(\s*[^>]*)>')





# ptrpar=re.compile(fr'<{tag}.*?(\w+)(?==).*?>')

ptrpar1=re.compile(fr'\b(\w+)(?==)')

tags = 'href="/wiki/World_Series" title="World Series'

# print(ptrpar1.findall(tags))
#========================================================

# results = re.compile(r'<(\w+)(|\s+[^>]*)>', re.I)

#pattern = re.compile(r'(?:<(\w+)(?:\s|>)|\s)(?:([a-z-]+)=(?:\'|"))?')

#==================================================================
s1='<li style="-moz-float-edge: content-box">... that <a href="/wiki/Orval_Overall" title="Orval Overall">Orval Overall</a> <i>(pictured)</i> is the only <b><a href="/wiki/List_of_Major_League_Baseball_pitchers_who_have_struck_out_four_batters_in_one_inning" title="List of Major League Baseball pitchers who have struck out four batters in one inning">Major League Baseball player to strike out four batters in one inning</a></b> in the <a href="/wiki/World_Series" title="World Series">World Series</a>?</li>'


# print(ptrtag.findall(s1))
#
# print(ptrtag.search(s1))
# print(ptrtagv1.findall(s1))
# print(results.search(s1))

# s = results.search(s1)
# print(s.groups())

ls1 = ptrtagv1.findall(s1)

print(ls1)

dc = {}


print("*"*100)
for item in ls1:

    print(type(item))

    print(item)


    lstag = ptrpar1.findall(item[1])

    print(type(lstag))
    print(lstag)

    dc[item[0]] = dc.get(item[0], []) + lstag






    # dc[item[0]] = dc.get(item[0], []) + item[1]

print(dc)

for item in sorted(dc.keys()):

    atrstr = ",".join(sorted(list(set(dc[item]))))

    print(f"{item}:{atrstr}")


d = set()

d.update()





