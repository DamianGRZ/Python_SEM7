class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def conjugate(self):
        self.imaginary = - self.imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return Complex(
        (self.real * other.real - self.imaginary * other.imaginary),
        (self.real * other.imaginary + self.imaginary * other.real)
                   )

    def __truediv__(self, other):
        divisor = other.real**2 + other.imaginary**2
        return Complex(
        (self.real * other.real + self.imaginary * other.imaginary)/(divisor),
        (self.imaginary * other.real - self.real * other.imaginary)/(divisor)
                   )
    def __eq__(self, other):
        if(self.real == other.real) and (self.imaginary == other.imaginary):
            return True
        else:
            return False

    def __str__(self):
        if self.imaginary >= 0:
            return "{0} + {1}j".format(self.real, self.imaginary)
        else:
            return "{0} {1}j".format(self.real, self.imaginary)

    #Calculator
def Calc(num1, num2, operation):
    num1 = num1.split()
    num2 = num2.split()
    print(num1)
    print(num2)
    num1 = Complex(int(num1[0]), int(num1[2].translate({ord('j'): None})))
    num2 = Complex(int(num2[0]), int(num2[2].translate({ord('j'): None})))
    match (operation):
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case _:
            print("This operation is not covered by this application")
            return Complex(0,0)

def printComplex(complex_number):
    if(complex_number.imaginary >= 0):
        print(complex_number.real, "+", complex_number.imaginary,'j')
    else:
        print(complex_number.real, complex_number.imaginary,'j')

