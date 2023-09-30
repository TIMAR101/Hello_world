def count_down_while_method(n):

    while n>=0:
        print(n)
        n-=1

count_down_while_method(50)
print("="*50)
#-------------------------------
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)
print(sys.getrecursionlimit())
def count_down_recursion(n):
    print(n)
    if n==0:
        return
    else:
        n=n-1
        count_down_recursion(n)

count_down_recursion(1000)

