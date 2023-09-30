class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        return sum([x for x in range(1,n+1) if n % x == 0])

"""List1 = [[l, g] for l in range(4) for g in range(4) if l < 2 and g > 2]
print(List1)

List1.sort()

odds = [x for x in squares if x % 2 != 0 ] # The snippet makes a list with only the odd elements of the squares list.
"""

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
