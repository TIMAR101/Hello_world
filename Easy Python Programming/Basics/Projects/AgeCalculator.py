dof = input("Enter the Data of Birth(yyyy/mm/dd: ")

y = dof[:4]

Age = 2023 - int(y)

print(Age)

print(y)

print(dof)

print("You are:   {0}  years old".format(Age))

print(f"You are: {Age} years old")
