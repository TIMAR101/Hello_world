"""(?=...)
Matches if ... matches next, but doesn’t consume any of the string.
This is called a lookahead assertion. For example, Isaac (?=Asimov)
will match 'Isaac ' only if it’s followed by 'Asimov'."""

regex = r'^(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})(?!.*(.).*\1)[\w]{10}$'

pattern = r'^(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)(?!.*(.).*\1)[a-zA-Z0-9]{10}$'

import re

data = "Isaac A1simov1"

data = "123AC12333"

ptr = re.compile(r"(?=[0-9a-z]*[A-Z]{2}[0-9a-z]*)[\w]{8}")

ptr = re.compile(r"(?=^[0-9a-z]*[A-Z][0-9a-z]*[A-Z][0-9a-z]*$)[0-9a-z]*[A-Z]")



ptr1 = re.compile(r"^(?=.*[A-Z]{2,})[\w]{8}")

#print(ptr1.search(data))   # (?=[A-Za-z]*[\d]{1,}[A-Za-z]*[\d]{1,})

ptr = re.compile(r"(?=[0-9a-z]*[A-Z]+[0-9a-z]*[A-Z]+)(?=[A-Za-z]*[\d]+[A-Za-z]*[\d]+[A-Za-z]*\d+)(?!.*(.).*\1)^[0-9a-zA-z]{10}$")

ptr = re.compile(r".*(.).*\1")

ptr = re.compile(r"(?=(.*[A-Z]){2,})[\w]+")


ptr = re.compile(r"(?=[0-9a-z]*[A-Z]+[0-9a-z]*[A-Z]+)(?=[A-Za-z]*[\d]+[A-Za-z]*[\d]+[A-Za-z]*\d+)^[0-9a-zA-z]{10}$")

#ptr = re.compile(r"(?=(.*[A-Z]){2,})[\w]+") (?!.*(.).*\1)

pattern = r'^(?!.*(.).*\1)(?=(.*[A-Z]){2,})(?=(.*\d){3,})[\w]{10}$'

#pattern = r'^(?=(.*[A-Z]){2,})((?=(.*\d){3,}))[\w]{10}$'

pattern = r'^(?!.*(.).*\1)[\w]{10}$'

ptr = re.compile(pattern)


data = "cdefgAZ123"
print(ptr.match(data))

print(ptr.search(data))


