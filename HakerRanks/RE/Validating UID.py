import re

pattern= re.compile(r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*[\d]){3,})[a-zA-Z0-9]{10}$')


regex = r'^(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})(?!.*(.).*\1)[\w]{10}$'

pattern = r'^(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)(?!.*(.).*\1)[a-zA-Z0-9]{10}$'

pattern=r'^(?=(?:.[A-Z]){2})(?=(?:.\d){3})(?!.(.).\1)[a-zA-Z0-9]{10}$' for i in range(n): if re.match(pattern,input()): print ('Valid') else: print('Invalid')
