secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

num = input("secret number: ")
num = int(num)

while num != secret_number:
    print("Ha ha! You're stuck in my loop!")
    num = int(input("secret number: "))

print("Well done, muggle! You are free now.")
