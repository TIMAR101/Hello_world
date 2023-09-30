#Replace all ______ with rjust, ljust or center.

#thickness = int(input()) #This must be an odd number
thickness = 5
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


s = "Tifofey Ryabinin"
print(s + "1")
s1=s.ljust(100, "+")
print(s1 + "1")
print(len(s1))

s2=s.center(20)
print(s2 + "1")
print(len(s2))

