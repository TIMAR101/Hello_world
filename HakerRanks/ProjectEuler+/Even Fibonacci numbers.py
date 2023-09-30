def fib(limit):

    sum = 0
    a=1
    b=1
    c=a+b
    while c < limit:
        sum = sum+c
        a=b+c
        b=c+a
        c=a+b
    return sum

print(fib(100))






