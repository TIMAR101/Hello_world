if __name__ == '__main__':

    Python_Students = []


    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     Python_Students.append([name, score])

    Python_Students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

    print(Python_Students)
    maxscore = 0
    secondscore = 0
    NamesList = []
    Scores = []


    for item in Python_Students:
        Scores.append(item[1])

    print(Scores)

    MinSscore = min(Scores)
    SecondScore = 0

    Scores.sort()
    print(Scores)

    for item in Scores:
        if item > MinSscore:
            SecondScore = item
            break

    print(SecondScore)

    for item in Python_Students:
        if item[1] == SecondScore:
            NamesList.append(item[0])

    NamesList.sort()
    print(NamesList)







