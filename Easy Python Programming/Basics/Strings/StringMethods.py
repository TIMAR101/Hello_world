st = "   Hello! Welcome to my Python tutorial!  "
  #"""0123456789"""

print(st)
print(st.title())
print(st.strip())

rs = st.lower()

print(st.count(" "))

print(type(st.count(' ')))

print(len(st))

rs = st.endswith('ial!')
print(rs)
ss = st.startswith('He')
print(ss)
print(type(ss))
print('*'* 100)

rs = st.replace('Hello', 'Hi!!!')
print(rs)

print(st.find("P"))

print(st.index("P"))

num = "1234569"
print(num.isnumeric())
