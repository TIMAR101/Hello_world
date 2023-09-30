class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here

    def computeDifference(self):

        lenElem = len(self.__elements)
        self.maximumDifference = 0

        for item1 in range(lenElem):

            for item2 in range(lenElem):
                if item1 != item2:
                    dif = abs(self.__elements[item1] - self.__elements[item2])
                    if dif > self.maximumDifference:

                        self.maximumDifference = dif

        return self.maximumDifference



# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
