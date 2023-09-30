def hammingWeight(n: int) -> int:

        StringNumber = str(n)

        count = 0

        for item in StringNumber:

            if item =="1":
                count+=1

        return count

def hammingWeight1(n: int) -> int: # n = 00000000000000000000000000001011
        return str(bin(n)).count("1")    # bin(n) = 0b1011

print(hammingWeight(101100000300000100000100040000000001000000000111))
print(hammingWeight1(101100000300000100000100040000000001000000000111))


