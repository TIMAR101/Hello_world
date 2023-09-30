dof = input("Enter the Date of Birth dd/mm/yyyy: ")

y = dof[-4:]

Age = 2023 - int(y)

print(f"You are {Age} years old")

print("You are  {0} years old".format(Age))
