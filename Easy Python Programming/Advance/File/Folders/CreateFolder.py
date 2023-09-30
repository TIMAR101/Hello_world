import os
#---------------------

r=os.path.exists("Data/Audio")

if r==True:
    print("The folder exists!")
else:
    os.mkdir("Data/Audio")
    print("Folder is created")


