import os


while True:
    CuId=input("Please enter the customrer Id: ")
    FileName = "Data/"+"info_"+CuId+".pxt"
    r=os.path.exists(FileName)
    if r==True:
        print("The file with this It is exist!!! Please enter another id!!")
    else:
        break

CuName=input("Pleaseenter the customrer Full Name: ")
CuGender=input("Pleaseenter the customrer Gender: ")
CuCell=input("Pleaseenter the customrer Cell: ")
#-------------------------------------------
FileName = "Data/"+"info_"+CuId+".pxt"
print(FileName)
#----------------generate customer data__________________
CuData=f"id= {CuId}\nName={CuName}\nGender={CuGender}\nCellNumber={CuCell}"
print(CuData)

f=open(FileName, "w")
f.write(CuData)
