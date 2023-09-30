regex_pattern = r"[\w]{3,3}\.[\w]{3,3}\.[\w]{3,3}\.[\w]{3,3}"	# Do not delete 'r'.

# ^(.{3}\.?){4}$

# r"(.{3}.){3}.{3}$"
# .{3}\..{3}\..{3}\..{3}
# ^(.{3}\.){3}.{3}$
# ^(...\.){3}...$
# p1 = re.compile(r'[0-3][\d]\.[0-1][\d]\.[1-2][\d]{1,3}')
import re
import sys

test_string = "123.456.abc.defddd"

test_string = "123.123.123.132.123.123"

match = re.match(regex_pattern, test_string)
print(match)

print(str(match).lower())
