"""Each new term in the Fibonacci sequence is generated by
adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose
values do not exceed four million, find the sum of the even-valued terms."""

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


i = 1
CurFib = 0

EvenSum = 0

while CurFib <= 4000000:

    CurFib = fib(i)

    if CurFib % 2 == 0:

        EvenSum+= CurFib

    i +=1

print(EvenSum)




