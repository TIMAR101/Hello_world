def is_prime(num):
    if num==1:
        return False
    elif num<4:
        return True
    elif num % 2 == 0:
        return False
    elif num < 9:
        return True
    elif num % 3 == 0:
        return False
    else:
        r = int(num**0.5)
        f=5
        while f <= r:
            if num % f==0 and num % (f+2) == 0 and num % (f+4) == 0:
                return False
            f = f + 8
        return True

#
# Write your code here.
#

for i in range(1, 50):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
