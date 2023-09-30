class Solution:
    def checkStraightLine(self, coordinates) -> bool:



        if len(coordinates) == 2:
            return True

        crossval = (coordinates[1][0] - coordinates[0][0])/abs(coordinates[1][1] - coordinates[0][1])

        for item in coordinates[2:]:

            if crossval != abs(item[0] - coordinates[0][0])/abs(item[1] - coordinates[0][1]):

                return False


        return True

    def checkStraightLine1(self, coordinates) -> bool:
        (x0, y0), (x1, y1) = coordinates[: 2]
        dx = x1 - x0
        dy = y1 - y0
        for x, y in coordinates[2:]:
            if dx * (y - y1) != (x - x1) * dy:
                return False
        return True

S1 = Solution()

print(S1.checkStraightLine1(coordinates = [[1,2],[2,3],[3,5]]))




