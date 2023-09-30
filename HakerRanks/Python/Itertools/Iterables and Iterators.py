
import itertools

k = 4

ls = ["a", "b", "c", "a", "d" ,"b" ,"z", "e", 'o']

#ls = ["a", "a", "c", "d"]


count = 0
count1 = 0

for item in itertools.combinations(ls, k):

    #print(item, end=" ")

    count1 += 1

    if "a" in item:
        count += 1

print(count/count1)

