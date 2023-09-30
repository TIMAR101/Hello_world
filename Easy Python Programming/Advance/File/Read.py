MyFile=open("Data/Info.dll", "r")
#MyFile.seek(17)
#Content=MyFile.read(20)
#Content=MyFile.readline(8)
#print(Content)
#Content=MyFile.readline(7)
#print(Content)
#Content=MyFile.readline(6)
Content=MyFile.readlines()

print(Content)
print(type(Content))

for x in Content:
    print(x.replace("\n", ''))



MyFile.close()
