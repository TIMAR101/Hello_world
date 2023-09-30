n = input()
lst = []

for i in range(n):
    cmd = input().split()  # insert 1 8. ## [insert, 1, 8]

    if cmd[0] == 'insert':
        lst.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'remove':
        lst.remove(int(cmd[1]))
    elif cmd[0] == 'append':
        lst.append(int(cmd[1]))
    elif cmd[0] == 'sort':
        lst.sort()
    elif cmd[0] == 'pop':
        lst.pop()
    elif cmd[0] == 'reverse':
        lst.reverse()
    elif cmd[0] == 'print':
        print(lst)


if __name__ == '__main__':
    elements = []
    for _ in range(int(input())):
        cmd, *arg = input().split()
        if cmd == 'insert':
            elements.insert(int(arg[0]), int(arg[1]))
        elif cmd == 'print':
            print(elements)
        elif cmd == 'remove':
            elements.remove(int(arg[0]))
        elif cmd == 'append':
            elements.append(int(arg[0]))
        elif cmd == 'sort':
            elements.sort()
        elif cmd == 'pop':
            elements.pop()
        elif cmd == 'reverse':
            elements.reverse()
