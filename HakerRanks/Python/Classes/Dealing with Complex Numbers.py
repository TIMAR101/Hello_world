import math

class Complex(object):
    def __init__(self, real, imaginary):

        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):

        num = Complex(self.real + no.real, self.imaginary+no.imaginary)
        return num

    def __sub__(self, no):

        num = Complex(self.real - no.real, self.imaginary-no.imaginary)
        return num

    def __mul__(self, no):

        num = Complex(self.real*no.real-self.imaginary*no.imaginary, self.real*no.imaginary+no.real*self.imaginary)

        return num

    def __truediv__(self, no):

        divisor = no.real**2 + no.imaginary**2
        real_part = (self.real * no.real + self.imaginary * no.imaginary) / divisor
        imag_part = (self.imaginary * no.real - self.real * no.imaginary) / divisor
        return Complex(real_part, imag_part)

    def mod(self):
        modulus = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(modulus, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')


n1 = complex(2,1)

n2 = complex(5,6)
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(abs(n1))
print(abs(n2))
