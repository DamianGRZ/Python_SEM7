from ast import Expression
import numpy as np
import unittest

class Complex:
    def __init__(self, realpart, imaginarypart):
        self.real = realpart
        self.imaginary = imaginarypart

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

class Calculator(unittest.TestCase):#asercja czy operacja siê wywowa³a, i kolejny test czy operacja jest prawid³owa
    def testAdd(self):
        Calc("1 + 2j", "1 + 1j", "+")

#EX5
if __name__ == "__main__":
    ## Complex numbers
    #print("----------------------------------------------------------")
    #print("Ex5.1, Complex number class and functions:")
    #num1 = Complex(2,1)
    #num2 = Complex(2,2)
    #complexaddresult = num1 + num2
    #complexsubresult = num1 - num2
    #print(complexaddresult.real, complexaddresult.imaginary,'j')
    #print(complexsubresult.real, complexsubresult.imaginary,'j')
    #printComplex(num1)
    # Calculator test
    #print("----------------------------------------------------------")
    #print("Ex5.2, Calculator test:")
    #using = True
    #while(using):
    #    print("Enter input in the format x + yj")
    #    num1 = input("Enter your first value: ")
    #    operation = input("Enter operation you want to do: ")
    #    num2 = input("Enter your second value: ")
    #    print(num1, operation, num2, end="")
    #    printComplex(Calc(num1, num2, operation))
    #    using = input("Do you want to continuee or exit(y/n): ")
    #    if(using != 'y'):
    #        using = False
    unittest.main();