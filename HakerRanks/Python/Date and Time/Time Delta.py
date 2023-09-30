"""Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000"""

"""from datetime import datetime as dt


fmt = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    print(int(abs((dt.strptime(input(), fmt) - 
                   dt.strptime(input(), fmt)).total_seconds())))"""

"""def time_delta(t1, t2):
    first = datetime.datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    second = datetime.datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    return str(abs(int((first-second).total_seconds())))"""

"""from dateutil import parser

for _ in range(int(input())):
    d1 = parser.parse(input().strip())
    d2 = parser.parse(input().strip())
    print(abs(int((d2-d1).total_seconds())))"""

import datetime
fmt = '%a %d %b %Y %H:%M:%S %z'

t1 = "Sun 10 May 2015 13:54:36 -0700"

d1 = datetime.datetime.strptime(t1, fmt)

print(d1)









