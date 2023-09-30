# Regex_Pattern = r"^([\d]{2}-?){4}$"	# Do not delete 'r'.
#
# Regex_Pattern = r"^[\d{8}|{\d]{2}(-?)([\d]{2}\1){2}[\d]{2}$"

#Regex_Pattern = r"^(\d{8}|\d{2}(?:-\d{2}){3})$"

# ^\d{2}(-?)(\d{2}\1){2}\d{2}$

# "^(\d{8}|\d{2}(?:-\d{2}){3})$"



#Regex_Pattern = r"^(\d{8}|\d{2}(-\d{2}){3})$"

Regex_Pattern = r"^(\d{8}|\d{2}(-)(\d{2}\2){2}\d{2})$"
import re

s = "12345678"

print(str(bool(re.search(Regex_Pattern, s))).lower())
