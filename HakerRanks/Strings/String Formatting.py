def print_formatted(number):

    # print(bin(number))

    """Decimal
Octal
Hexadecimal (capitalized)
Binary"""

    N =  (len(bin(number)))

    for item in range(1, number+1):

        print("{0:d}".format(item), end="")

        print(" " * (N - len("{0:d}".format(item))), end="" )

        print("{0:o}".format(item), end="")

        print(" " * (N - len("{0:o}".format(item))), end="" )

        print("{0:x}".format(item), end="")

        print(" " * (N - len("{0:x}".format(item))), end="" )

        print("{0:b}".format(item), end="\n")


def print_formatted1(number):

    width  =  (len(bin(number)))-2

    for num in range(1,number+1):

        decimal = str(num).rjust(width)
        octal = oct(num)[2:].rjust(width)
        hexadecimal = hex(num)[2:].upper().rjust(width)
        binary = bin(num)[2:].rjust(width)
        row = [decimal, octal, hexadecimal, binary]
        print(" ".join(row))








# int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)

print_formatted(17)

print_formatted1(17)



