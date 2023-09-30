# Prompt the user to enter a word
# and assign it to the user_word variable.
"""use conditional execution and the continue statement
to "eat" the following vowels A, E, I, O, U from the inputted word;"""

word_without_vowels = ""

user_word = input("Enter userword: ")
user_word = user_word.upper()
MyList = ["A", "E", "I", "O", "U"]

for letter in user_word:
    if letter in MyList:
        continue
    else:
        word_without_vowels += letter

    print(letter)

print(f"world without eaten letter is: \n{word_without_vowels}")


    # Complete the body of the for loop.

