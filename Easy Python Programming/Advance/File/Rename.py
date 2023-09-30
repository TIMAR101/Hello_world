import os

r=os.path.exists("Data/Test.txt")

if r==True:
    print("The file exists!!!")
    print("I will rename this file")
    os.rename("Data/Test.txt", "Data/TestNew.txt")
else:
    print("The file not exists")
    print("I will not rename...")


