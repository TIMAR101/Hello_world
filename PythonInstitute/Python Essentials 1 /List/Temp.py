hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
print(hat_list)
a=int(input("plese enter the number of element: "))
b=int(input("Please enter the meaning of the element: "))

hat_list[a]=b
print(hat_list)

# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]

# Step 3: write a line of code that prints the length of the existing list.
print(f"The lenght of the list is {len(hat_list)}")

print(hat_list)

a= 1
b = 2
a, b = b, a

print(a, b)
