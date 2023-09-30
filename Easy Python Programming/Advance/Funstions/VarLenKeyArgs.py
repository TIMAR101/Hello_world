def MyMistress(**Mistress):
    Name=Mistress['Fname']
    Num=Mistress["Number"]
    Kind=Mistress["Kind"]
    print(Mistress)
    print(type(Mistress))
    print(f"Hi my mistress {Name}. You are {Num}. You are best in {Kind}")


#------------------------------

MyMistress(Fname="Natasha", Number=1, Kind="blowjob")
MyMistress(Kind="Anal",Fname="Lena", Number=1)
MyMistress(Number=1, Kind="On top", Fname="Inna")
