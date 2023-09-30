def countingValleys(steps):

    level = 0

    valey = 0

    flag = 0

    stepdict = {"U":1, "D":-1}

    for step in steps:

        level += stepdict[step]

        if level < 0 and flag >=0:

            valey +=1

            flag = -1

        if level >= 0:
            flag = 1

    return valey

print(countingValleys("UDDDUDUU"))




