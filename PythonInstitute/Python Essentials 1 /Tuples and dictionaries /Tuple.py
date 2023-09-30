one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,

print(one_element_tuple_1)

print(one_element_tuple_2)

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

a="My name is Timofey!!!"

a = tuple(a)

print(a)
