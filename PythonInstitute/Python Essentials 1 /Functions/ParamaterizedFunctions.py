def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

introduction(first_name="Timofey", last_name="Ryabinin")

introduction()
introduction(last_name="Hopkins")

def add_numbers(a, b=2, c):
    print(a + b + c)

add_numbers(a=1, c=3)

