"""Imagine a list - not very long, not very complicated,
just a simple list containing some integer numbers.
Some of these numbers may be repeated, and this
is the clue. We don't want any repetitions. We want them to be removed.

Your task is to write a program which removes all the number
repetitions from the list. The goal is to have a
list in which all the numbers appear not more than once."""


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print(my_list)



#
# Write your code here.

new_list = []

number = 0

for num1 in my_list:

    if num1 not in new_list:
        new_list.append(num1)

#
print("The list with unique elements only:")
print(my_list)
print(new_list)


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

temp_list = my_list.copy()


for t1 in my_list:

    while t1 in my_list:
        my_list.remove(t1)

    else:
        my_list.append(t1)



print(my_list)
