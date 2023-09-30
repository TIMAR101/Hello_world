def nearestValidPoint(x: int, y: int, points) -> int:

        MinDist = 9999999999999999999999
        count = 99999999999999

        for item in range(len(points)):

            x1 = points[item][0]
            y1 = points[item][1]

            if x == x1 or y ==y1:

                if MinDist > abs(x1 - x) + abs(y1 - y):

                    MinDist = abs(x1- x) + abs(y1 - y)
                    count = item






        return -1 if  count == 99999999999999 else count

print(nearestValidPoint(3, 4, [[1,2],[3,1],[2,4],[2,3],[4,4]]))
