#Write your code here
class Calculator:
    def power(self, n, p):
        if n<0 or p<0:
            raise ValueError("n and p should be non-negative")
        else:
            return pow(n, p)


myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)

r1= range(4)
r2 = range(4)

m1 = map(pow, r1, r2)

print(list(m1))

