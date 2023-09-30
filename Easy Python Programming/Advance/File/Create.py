import os

r = os.path.exists("Data/Info4")

if r==True:
    print("The file exists!!!")

else:
    MyFile=open("Data/Info4", "x")
    MyFile.close()
    print("I've created the file")

