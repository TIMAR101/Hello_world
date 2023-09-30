# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
# m = re.search(r"(?<=<)\w(?=>)", "<a>")
#p = re.compile(r'((?<=<)(?P<tag1>[A-z])(?=>.*</(?P=tag1)>)) | ((?<=<)(?P<tag2>[A-z])(?=.*>.*</(?P=tag2)>))')

#p = re.compile(r'(?<=<)\s*(?P<tag1>[A-z]+)(?=.*>.*</(?P=tag1)>)')

p = re.compile(r'(?<=<)\s*([A-z]+)(?=.*>.*<\s*/(?:\1)\s*>)')

p = re.compile(r'(?<=<)\s*(\w+)')



s1 = '<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>'

s2 = '<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>'
s3 = '<p>This is a paragraph</p>'
s4 = '<  p  >This is also a paragraph</p>'
s5 = '<a href="http://www.google.com">Google < /a >'
s6 = '<p></p>'
print(p.findall(s1))

print(p.findall(s2))
print(p.findall(s3))
print(p.findall(s4))
print(p.findall(s5))
print(p.findall(s6))

st = []
#
for ___ in range(int(input())):

    data = input()

    ls = p.findall(data)

    st.extend(ls)


st = list(st).sort()

print(",".join(st))



