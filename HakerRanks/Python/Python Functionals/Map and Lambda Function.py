# cube = lambda x: x*x*x # complete the lambda function

def fibonacci(n):


     # return a list of fibonacci numbers
     lis = [0,1]
     for i in range(2,n):
         lis.append(lis[i-2] + lis[i-1])
     return(lis)

def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

print(list(map(cube, list(fibonacci(inp)))))

fib = lambda y: y if y < 2 else fib(y - 1) + fib(y - 2)
print map(lambda x: x**3, map(fib, range(input())))

#Code with comment:

#1. lambda function to find cube of a number:
cube = lambda x: x*x*x

#2. fibonacci function to find the fibonacci series:
def fibonacci(n):
    #Initialising the first 2 variables of the series:
    a,b = 0,1
    #for loop to find the fibonacci series upto n terms:
    for i in range(n):
        yield a
        a,b = b,a+b

fib = [0, 1]
[fib.append(sum(fib[-2:])) for x in range(n)]
return fib[:n]


fib=[0,1]
n= int(input())
for i in range(2,n):
    fib +=[sum(fib[-2:])]
print(list(map(lambda x:x**3,fib[:n])))

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

print(fibonacci(5))

cube = lambda x:x**3  # complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    list = []

    for i in range(n):

        if(i == 0):
            x = 0
            list.append(x)
        elif(i == 1):
            x = 1
            list.append(x)
        else:
            x = list[i - 1] + list[i - 2]
            list.append(x)

    return list
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


cube = lambda f: f**3

def fibonacci(n):
    value = 0
    step = 1

    for _ in range(n):
        yield value
        value, step = step, value + step

















