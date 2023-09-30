MyFile=open("Data/Info2.mp3", "wt") #w
#============================================
#r=MyFile.write("Hello Python!!! \nI love you"+"\nYou're great!!!")
#r=MyFile.writelines(["Hello Python", "\nI love you!!!", "\nYou love you"] )
MyFile.seek(10)
r=MyFile.write("Hello Python!!! \nI love you"+"\nYou're great!!!")
print(r)
#-------------------------------------------
MyFile.close()
MyFile=open("Data/Info2.mp3", "rt")
Content = MyFile.read()
print(Content)
MyFile.close()
