import calendar
from datetime import datetime

# print(calendar.TextCalendar())
# print(calendar.TextCalendar(firstweekday=7).formatyear(2030))

days = {0: "MONDAY", 1: "TUESDAY", 2: "WEDNESDAY", 3: "THURSDAY", 4:"FRIDAY", 5: "SATURDAY", 6 :"SUNDAY"}
# days = {0: "MONDAY", 1: "TUESDAY", 2: "WEDNESDAY", 3: "THURSDAY", 4:"FRIDAY", 5: "SATURDAY", 6 :"SUNDAY"}
#
# print(calendar.weekday(year, month, day))
#
# print(days[calendar.weekday(year, month, day)])
#02 29 2004

day, month, year = 29,2, 2004
print(calendar.weekday(year, month, day))

n = calendar.weekday(year, month, day)

print(days[calendar.weekday(year, month, day)])

print(calendar.day_name[n])



print(list(calendar.day_name)[calendar.weekday(year, month, day)].upper())

print(datetime(year, month, day).strftime("%A").upper())

