"""I, V, X, L, C, D, and M, standing respectively for 1, 5, 10, 50, 100, 500"""

regex_pattern = r"^C?M{,3}(CM|C)?D{,3}X?C{,3}X?L?I?X{,3}I?V?I{,3}$"  # Do not delete 'r'.

regex_pattern = r"M{,3}(D?C{,3}|C[DM])?(L?X{,3}|X[LC])?(V?I{,3}|I[VX])?$"
	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))
