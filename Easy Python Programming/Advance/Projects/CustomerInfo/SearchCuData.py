import os

CuId=input("Plese input the customer Id:")

FileName = "Data/"+"info_"+CuId+".pxt"

r=os.path.exists(FileName)
if r==True:
    print("The file with this Id is exist!")
    print("Loading data:")
    f=open(FileName, "r")
    CuData=f.read()
    print(CuData)

    f.close()
else:
    print("The file is nof found!!")
