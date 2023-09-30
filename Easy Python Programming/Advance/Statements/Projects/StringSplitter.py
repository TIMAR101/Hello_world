x = "Hello Python!"

print(len(x))
l = len(x)
index = 0
#---------------------

while index < l:
    a = x[index]
    print(a)
    #____________-
    index +=1

else:
    print(f"It's done! Number of letter is {l}. And current index is {index}")


#===============================================================================

#reverse indexing

ri = 0 - l



while ri != 0:

    #print(ri)

    print(x[ri])

    ri +=1

else:
    print(ri)



ri = 0 - l

i = -1

while i >= ri:

    print(x[i])

    i -= 1
else:
    print(i)





