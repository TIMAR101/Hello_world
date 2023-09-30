MyFile=open("Data/Info_ra.txt", "a+")

r=MyFile.write("Hello Read-Append in Python!")
MyFile.seek(0)
Content=MyFile.read()
print(Content)

MyFile.close()
