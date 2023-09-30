def maxfactor(n):

    if n % 2 ==0:
        lastFactor = 2
        n = n //2
        while n % 2 == 0:
            n = n//2

    else:
        lastFactor = 1
    factor = 3
    maxFactor = n**0.5

    while n >1 and factor <=maxFactor:
        if n % factor == 0:
            n = n//factor
            lastFactor = factor
            while n % factor==0:
                n = n//factor
            maxFactor = n**0.5

        factor += 2

    if n == 1:
        return lastFactor
    else:
        return n

print(maxfactor(17))




