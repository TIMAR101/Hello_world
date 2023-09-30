CurrentTry=1
TotalGuesses=3
CorrectAnswer="Horse"

#-----------------------------------
while CurrentTry<=TotalGuesses:
    UserAnswer=input(f"Guess the animal name starting with '{CorrectAnswer[0]} :")
    #---------------------------------
    UserAnswer=UserAnswer.replace(" ", '')
    UserAnswer=UserAnswer.replace(UserAnswer[0], UserAnswer[0].upper())
    print(f"Your formatted answer is {UserAnswer}")
    if UserAnswer=="":
        print("Wrong empty input!!! Please input correct answer!!!")
        continue

    if UserAnswer==CorrectAnswer:
        print("Correct answer!!! You're wonderful!!!")
        print("You have used {0} attempts".format(CurrentTry))
        break
    else:

        print("Wrong answer!!! Please repeat answer. Left {0} of {1} attempts".format((TotalGuesses-CurrentTry), TotalGuesses))
        print(f"Wrong answer!!! Please repeat answer. Left {TotalGuesses - CurrentTry} of {TotalGuesses} attempts")
        CurrentTry+=1

else:
    print("You lost this games!!!")
