# Enter your code here. Read input from STDIN. Print output to STDOUT

for ___ in range(int(input())):

    try:

        a,b = input().split()
        print(eval(f"{a}/{b}"))

    except Exception as e:

        print(f"Error Code,{e.value}")




