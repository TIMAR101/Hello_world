def Mydec(anyFunction):

    def changer(*args):

        print("I am changer!!!!")

        return "Excellent"

    return changer

@Mydec
def sum1(a1, a2):

    return a1 + a2

def dif1(b1, b2):

    return b1-b2

print(sum1(5,2))

print(dif1(5,2))









