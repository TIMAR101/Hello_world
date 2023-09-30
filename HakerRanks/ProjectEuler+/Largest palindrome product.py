def isPalindrome(n):

    return list(str(n)) == list(str(n))[::-1]


def maxPalindrome(n):

    while True:

        if isPalindrome(n):
            return n
        else:
            n -= 1

def largestPalindrome(n):

    lagPal = 0

    for a in range(999,99,-1):

        for b in range(999,99,-1):

            t = a*b


            if t > n:
                continue

            if t <= lagPal:
                break



            if isPalindrome(t):
                lagPal = t

    return lagPal





print(largestPalindrome(800000))
