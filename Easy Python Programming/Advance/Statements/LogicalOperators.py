EmpName = "Mj"
EmpAge = 19

#===============================================================

if EmpName == "Mj" and EmpAge >= 19:
    print("This is valid eployee!!!")

else:
    print("This is not valid employee")
#--------or operator-------------------------------

EmpName = "Mj1"
EmpAge = 5

if EmpName == "Mj" or EmpAge >= 19:
    print("This is valid eployee!!!")

else:
    print("This is not valid employee")

#---------------------------not operator---------------------------

b = False
print(not(b))

#----------------------------last example------------------------

EmpName = "Mj1"
EmpAge = 18

if not(EmpName == "Mj" or EmpAge >= 19):

    print("This is valid employee!!!")
else:
    print("This is not valid employee!!!")









