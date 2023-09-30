import os

r=os.path.exists("Data/TestDel.txt")
while True:
    if r==True:
        os.remove("Data/TestDel.txt")
        print("It's done!!!")

    else:
        print("It's not found")
        MyFile=open("Data/TestDel.txt", "x")
        MyFile.close()
        print("I've created the file")
