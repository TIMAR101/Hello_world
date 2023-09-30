# Enter your code here. Read input from STDIN. Print output to STDOUT

t = "Timofey"
t1 = t[::-1]
print(t1)

N, data = input(), input().split()

print(all(int(item) > 0 for item in data) )

print(any(item1 == item1[::-1] for item1 in data))

print(all(int(item) > 0 for item in data) and any(item1 == item1[::-1] for item1 in data))
print( all(int(item) > 0 for item in data) and any(list(str(item1)) == list(str(item1)).reverse() for item1 in data))


t = "Timofey"
