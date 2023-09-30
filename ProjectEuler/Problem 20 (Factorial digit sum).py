def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

def rec_factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * rec_factorial_function(n - 1)




FactTen = rec_factorial_function(100)
sum = 0

for dt in str(FactTen):

    sum+=int(dt)

print(sum)

