import os
r=os.path.exists("Data/Pics")

if r==True:
    print("The folder exists!!!")
else:
    print("Folder not found")
