import Howmanydays as hd


def day_of_year(year, month, day):

    if month < 1 or month > 12 or day < 1 or day > 31 or year < 1 or year >= 2023:
        return None

    days = 0

    for n in range(1, month):

        days += hd.days_in_month(year, n)

    md = hd.days_in_month(year, month)

    if day > 0 and day <= md:
        days += day
    else:
        return None

    return days


#
# Write your new code here.
#

print(day_of_year(2000, 12, 31))

print(day_of_year(2000, 12, 31))
