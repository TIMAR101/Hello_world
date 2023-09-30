import os
#---------------------------------------------
r=os.path.exists("Data/Audio")

if r==True:
    print("The folder exists")
    print('I will rename it!!!')
    os.rename("Data/Audio", "Data/Audio1")
else:
    print("Folder not found")
    os.rename("Data/Audio1", "Data/Audio")




