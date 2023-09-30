a="Irina"
c="Natasha"
def test():
    a="Aliya"
    print(a)
    global Lname
    Lname="Anna"

    global c
    c="Inna"


#--------------------------------------------
test()
print(a)
print(c)
print(Lname)



