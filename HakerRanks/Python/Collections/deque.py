from collections import deque
d = deque()
for _ in range(int(input())):
    op = input().split(' ')
    eval(f"d.{op[0]}({op[1]})") if "pop" not in op[0] else eval(f"d.{op[0]}()")
print(*d)


from collections import deque

n = int(input().strip())
d = deque()

commands = {
    'append': lambda x: d.append(x),
    'pop': lambda : d.pop(),
    'appendleft': lambda x: d.appendleft(x),
    'popleft': lambda : d.popleft()
}

for i in range(n):
    comm, *args = input().split()

    operation = commands.get(comm, lambda : None)

    result = operation(*map(int, args))


print(*[x for x in d], end = ' ')

from collections import deque

N = int(input()) # Number of operations

queue = deque()
for _ in range(N):
    operation = input().split()
    func = getattr(queue, operation[0])

    if(len(operation) == 1):
        func()
    else:
        func(int(operation[1]))

print(*queue, sep=" ")

from collections import deque
no = int(input())
d = deque()
for i in range(no):
        name,*no = input().split()
        eval('d.{}({})'.format(name,str(*no)))
print(*d)

from collections import deque

d = deque()
funs = {'append': deque.append, 'pop': deque.pop, 'popleft': deque.popleft, 'appendleft': deque.appendleft}

n = int(input())
for _ in range(n):
    cmd, *args = input().split()
    fun = funs.get(cmd)
    if args:
        fun(d, *args)
    else:
        fun(d)
print(' '.join(d))

d = deque()

N = int(input())
for i in range(N):
    line = input().split(' ')
    method = line[0]
    try:
        arg = line[1]
    except:
        #No argument found. Execute method without argument
        eval(f'd.{method}()')
    else:
        eval(f'd.{method}({arg})')
print(*d)
