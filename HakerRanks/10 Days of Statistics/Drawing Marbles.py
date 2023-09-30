"""A bag contains 3  red marbles and 4  blue marbles.
Then, 2  marbles are drawn from the bag, at random,
without replacement. If the first marble drawn is red,
what is the probability that the second marble is blue?"""

"""Total possibilities = 7
Total possibilities after drawing red = 6
Possibilities of one blue marble = 1/6
Possibilities of 4 blue marble = 4/6 = 2/3"""

"""There are  possible events in our sample space:

 passes the exam and  fails ().
 passes the exam and  fails ().
 and  both pass the exam ().
 and  both fail the exam ().

Approach 1:
We are only concerned with the first  events (). 
First, we calculate . Because one student's 
test grade does not depend on another 
student's test grade,  and  are independent 
and we can say that the probability of both 
students passing the exam is . Now that we 
know the probability of both students passing 
the exam, we can determine the probability of a
t least  student passing the exam:
all bals red = 3/7 * 3/ 7 = 9/49
all bals blue 4/7*4/7 = 16/49
 bals red one blue 3/7*4/7 = 


"""

ans = []
frq = []
allbals = []

allred =[]
allblue =[]



import fractions

bag = ["R1", "R2", "R3", "B1", "B2", "B3", "B4"]

for b1 in range(len(bag)):

    for b2 in range(len(bag)):

        if b1 == b2:
            continue
        allbals.append((bag[b1], bag[b2]))
        if "R" in bag[b1] and   "R" in bag[b2]:
            allred.append((bag[b1], bag[b2]))
        elif "B" in bag[b1] and   "B" in bag[b2]:
            allblue.append((bag[b1], bag[b2]))
        else:
            ans.append((bag[b1], bag[b2]))






print("All ball is Red:", fractions.Fraction(len(allred), len(allbals)))

print("All ball is Blue:", fractions.Fraction(len(allblue), len(allbals)))

print("All ball is Different:", fractions.Fraction(len(ans), len(allbals)))

print("Solution", fractions.Fraction(len(allred), len(ans)))

print(frq)

print(ans)








