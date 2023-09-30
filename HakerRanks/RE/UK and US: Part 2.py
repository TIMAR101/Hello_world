# Enter your code here. Read input from STDIN. Print output to STDOUT
import re



ptrse = re.compile(r"our")

# data="the odour coming out of the left over food was intolerable ammonia has a very pungent odor"
#
# data1 = "odour"
#
# print(ptrse.search("odour"))
#
# data2 = ptrse.sub("or", data1)
#
# print(data2)
#
# print(re.findall(rf"({data1}|{data2})", data))







data = "\n".join(input() for __ in range(int(input())))

#print(data)

for ___ in range(int(input())):

    template = input().strip()

    if ptrse.search(template):

        template1 = ptrse.sub("or", template)

        #print(template, template1)

        print(len(re.findall(fr'({template1}|{template})', data)))

    else:


        print(re.findall(rf'{template}', data))



