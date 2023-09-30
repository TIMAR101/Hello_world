

n = int(input().strip())

print(sum(item for item in range(3, n+1) if (item%3 ==0 or item%5 == 0)))


"""target=999
Function SumDivisibleBy(n)
 p=target div n
 return n*(p*(p+1)) div 2
EndFunction
Output SumDivisibleBy(3)+SumDivisibleBy(5)-SumDivisibleBy(15) """

def SumDivisibleBy(t, n):
        p = t//n
        return n*(p*(p+1)) // 2

print(SumDivisibleBy(10,3)+SumDivisibleBy(10,5)-SumDivisibleBy(10,15))

