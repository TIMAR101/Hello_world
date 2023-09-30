blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#
height=0
curblock=0
cur_lay=1
while cur_lay<= blocks:
    height += 1
    blocks -= cur_lay
    cur_lay += 1





print("The height of the pyramid:", height)




