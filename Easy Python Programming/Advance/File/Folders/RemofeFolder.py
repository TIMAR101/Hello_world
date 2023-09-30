import os


r=os.path.exists("Data/Audio")
if r==True:
    os.rmdir("Data/Audio")
    print("I have removed this direcotry")
else:
    os.mkdir("Data/Audio")
    print("I've created this directory")
