import numpy as np
class Complex:
    def __init__(self, realpart, imaginarypart):
        self.real = realpart
        self.imaginary = imaginarypart
    def conjugate(self):
        self.imaginary = - self.imaginary

def add_complex_numbers(number1, number2):
    return Complex(number1.real + number2.real, number1.imaginary + number2.imaginary)

def sub_complex_numbers(number1, number2):
    return Complex(number1.real - number2.real, number1.imaginary - number2.imaginary)

def mul_complex_numbers(number1, number2):
    return Complex(
        (number1.real * number2.real - number1.imaginary * number2.imaginary),
        (number1.real * number2.imaginary + number1.imaginary * number2.real)
                   )
def div_complex_numbers(number1, number2):
    divisor = number1.real**2 + number1.imaginary**2
    return Complex(
        (number1.real * number2.real - number1.imaginary * number2.imaginary)/(divisor),
        (number1.real * number2.imaginary + number1.imaginary * number2.real)/(divisor)
                   )
    #Calculator
def Calc(expression):
    ex = expression.strip()
    ex = expression.split()
    if(ex[0].find('j') == -1):#not found
        num1 = Complex(int(ex[0]), 0)
    else:
        num1 = Complex(0, int(ex[0]))
    for i in range(1, len(ex), 2):
        if(ex[i+1].find('j') == -1):#not found
            num2 = Complex(int(ex[i+1].translate({ord('j'): None})), 0)
        else:
            num2 = Complex(0, int(ex[i+1].translate({ord('j'): None})))
        if ex[i] == '+':
            num1 = add_complex_numbers(num1, num2)
        elif ex[i] == '-':
            num1 = sub_complex_numbers(num1, num2)
        elif ex[i] == '*':
            num1 = mul_complex_numbers(num1, num2)
        elif ex[i] == '/':
            num1 = div_complex_numbers(num1, num2)
    return num1

def printComplex(complex_number):
    if(complex_number.imaginary >= 0):
        print(complex_number.real, "+", complex_number.imaginary,'j')
    else:
        print(complex_number.real, complex_number.imaginary,'j')
#EX5
if __name__ == "__main__":
    # Complex numbers
    print("----------------------------------------------------------")
    print("Ex5.1, Complex number class and functions:")
    num1 = Complex(2,1)
    num2 = Complex(2,2)
    complexaddresult = add_complex_numbers(num1, num2)
    complexsubresult = sub_complex_numbers(num1, num2)
    printComplex(num1)
    # Calculator test
    print("----------------------------------------------------------")
    print("Ex5.2, Calculator test:")
    print(complexaddresult.real, complexaddresult.imaginary,'j')
    print(complexsubresult.real, complexsubresult.imaginary,'j')
    print("2 + 3j + 10 = ", end="")
    printComplex(Calc("2 + 3j + 10"))