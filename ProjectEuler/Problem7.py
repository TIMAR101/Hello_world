"""By listing the first six prime numbers: 2, 3, 5, 7, 11,
and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""


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
            if n % f==0 and n % (f+2) == 0 and n % (f+4) == 0:
                return False
            f = f + 8
        return True

nmax = 10001
n = 0
CurNum = 2
CurPrime = 2

while n <= nmax:

    if is_prime(CurNum):
        n = n + 1
        CurPrime = CurNum
    CurNum = CurNum+1

print(f"n = {n} CurNum = {CurNum} CurPrime = {CurPrime}")

