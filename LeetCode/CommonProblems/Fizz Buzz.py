class Solution:
    def fizzBuzz(self, n: int):

        OutList = []

        for item in range(1, n+1):

            if item % 3 == 0 and item % 5 == 0:
                OutList.append("FizzBuzz")

            elif item % 3 == 0:
                OutList.append("Fizz")

            elif item % 5 == 0:
                OutList.append("Buzz")

            else:
                OutList.append(str(item))

        return OutList

class Solution1:
    def fizzBuzz(self, n: int):
        f, b, fb = 'Fizz', 'Buzz', 'FizzBuzz'
        arr = [str(x + 1) for x in range(n)]

        for i in range(2, n, 3):
            arr[i] = f

        for i in range(4, n, 5):
            arr[i] = b

        for i in range(14, n, 15):
            arr[i] = fb

        return arr

for i in range(2, 30, 3):
    print(i, end=" ")
