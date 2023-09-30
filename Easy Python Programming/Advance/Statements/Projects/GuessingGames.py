CurrentTry=1
TotalGuesses = 3
CorrectAnswer=7
#-------------------------

while CurrentTry<=TotalGuesses:
    UserAnswer = input("Enter your guess: (Between 0 ... 9):")
    UserAnswer=UserAnswer.replace(" ", '')
    if UserAnswer.isnumeric()==False or UserAnswer=="":
        print("Please enter numeric input!!!")
        continue
    UserAnswer=int(UserAnswer)
    if UserAnswer<0 or UserAnswer>9:
        print("PLese enter number between 0 ... 9!!!!")
        continue

    if UserAnswer==CorrectAnswer:
        print("You win!!!")
        break
    else:
        print(f"Wrong Answer! Try again! Left {TotalGuesses-CurrentTry} of {TotalGuesses}")
    #----------------------------------------------------
    CurrentTry+=1  # CurrenTry = CurrentTry + 1

else:
    print("You are lost!!!")
