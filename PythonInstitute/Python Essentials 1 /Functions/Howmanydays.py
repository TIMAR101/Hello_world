def is_year_leap(year):

    if (year % 400 == 0) and (year % 100 == 0):
        return True

    elif (year % 4 == 0) and (year % 100 != 0):
        return True

    else:
        return False


def days_in_month(year, month):

    DayInMonth = [31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2:

        if is_year_leap(year):
            return DayInMonth[1][1]
        else:
            return DayInMonth[1][0]

    elif month > 0 and month <= 12:

        return DayInMonth[month-1]

    else:
        return None


#
# Write your new code here.
#

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
