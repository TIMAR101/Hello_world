import fractions

X = ["R", "R", "R", "R", "B", "B", "B"]
Y = ["R", "R", "R", "R", "R", "B", "B", "B", "B"]
Z = ["R", "R", "R", "R", "B", "B", "B", "B"]
ans = []
frq = []
count = 0

for i in range(len(X)):
    for j in range(len(Y)):
        for k in range(len(Z)):
            frq.append([X[i], Y[j], Z[k]])
            ans = [X[i], Y[j], Z[k]]
            if ans.count("R") == 2:
                if ans.count("B") == 1:
                    count += 1

print(count)
print(len(frq))

answer = count/len(ans)

answer1 = fractions.Fraction(count, len(frq))
print(answer1)




















print(answer)
