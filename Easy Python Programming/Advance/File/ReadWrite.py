MyFile=open("Data/Info_rw.txt", "r+")
#------------------------------------------

r=MyFile.write("Hello Reat Write in Python!")
MyFile.seek(0)
Content=MyFile.read()
print(Content)
