def my_function(my_list_1):
    global my_list_2

    my_list_2[1] = "555"


    


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

