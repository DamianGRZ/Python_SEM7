from copy import deepcopy
import math
import random
import numpy as np

# Obliczenia
def quadratic_equation(a, b, c):
    discriminant = pow(b, 2) - 4 * a * c
    if discriminant > 0:
        x1 = -b - math.sqrt(discriminant) / (2 * a)
        x2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        return -b / (2 * a)
    elif discriminant < 0:
        x1 = x2 = -b / (2 * a)
        im = math.sqrt(-discriminant) / (2 * a)
        return {x1, im}, {x2, im}


def sort(toSort):
    listLenght = len(toSort)
    for i in range(listLenght, 0, -1):
        for j in range(listLenght - 1, listLenght - i, -1):
            if toSort[j] > toSort[j - 1]:
                toSort[j], toSort[j - 1] = toSort[j - 1], toSort[j]
    print(toSort)


def scalarProduct(a, b):
    scalarProduct = 0
    for index in range(0, len(a)):
        scalarProduct = scalarProduct + a[index] * b[index]
    return scalarProduct


def matrix_sum(m1, m2):
    if len(m1[0]) == len(m1[0]) and len(m1) == len(m2):
        return [
            [m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))
        ]
    else:
        print("Matrices are not of the same dimensions")
        return 0


def matrix_mul(m1, m2):
    result = np.random.randint(1, size=(128, 128))  # zeros array
    if len(m1[0]) == len(m2):
        for row in range(len(m1[0])):
            for col in range(len(m1)):
                for i in range(len(m2)):
                    result[row][col] += m1[row][col] * m2[i][col]
        return result
    else:
        return "Sorry, wrong dimensions"

def sub_matrix(matrix, row, column):
    sub_matrix = matrix[:]
    sub_matrix = np.delete(sub_matrix, 0, axis=0)  # Delete row
    sub_matrix = np.delete(sub_matrix, column, axis = 1) #delete column
    return sub_matrix

def matrix_determinant(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    if(num_rows != num_cols):
        print("Not a square matrix")
        return None
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    else:
        det = 0
        for col in range(num_cols):
            sign = (-1) ** (0 + col)
            det += sign * matrix[0][col] * matrix_determinant(sub_matrix(matrix, 0, col))

    return det


# EX4
if __name__ == "__main__":
    # quadratic_equation
    print("----------------------------------------------------------")
    print("Ex4.1, calculate quadtratic equation (y = ax2+bx+c) roots:")
    print("One root: ")
    print("The equation is: y = x2-10x+5 = ")
    print(quadratic_equation(1, -10, 5))
    print("Two roots: ")
    print("The equation is: y = x2+3x+2 ")
    print(quadratic_equation(1, 3, 2))
    print("Two complex roots: ")
    print("The equation is: y = 4x2+3x+2 ")
    print(quadratic_equation(4, 3, 2))

    # sort
    print("----------------------------------------------------------")
    print("Ex4.2, sort random numbers in descending order:")
    randomList = random.sample(range(1, 100), 50)
    print("List before sorting:")
    print(randomList)
    print("List after sorting:")
    sort(randomList)

    # scalarProduct
    print("----------------------------------------------------------")
    print("Ex4.3, caluclate scalar product of 2 given matrices:")
    A = [1, 2, 12, 4]
    B = [2, 4, 2, 8]
    print("First: ", *A)
    print("Second: ", *B)
    product = scalarProduct(A, B)
    print("Scalar Product = ", product)
    if product == np.dot(A, B):
        print("Result is correct, checked with numpy")
    else:
        print("Result is incorrect, checked with numpy")

    # Matrix Sum
    print("----------------------------------------------------------")
    print("Ex4.4, caluclate matrix sum of 2 matrices 128x128:")
    randomMatrix1 = np.random.randint(3, size=(128, 128))
    randomMatrix2 = np.random.randint(3, size=(128, 128))
    matrixSum = matrix_sum(randomMatrix1, randomMatrix2)
    print(matrix_sum(randomMatrix1, randomMatrix2))
    # Matrix multiplication
    print("----------------------------------------------------------")
    print("Ex4.5, caluclate matrix multiplication of 2 matrices 8x8:")
    randomMatrix3 = np.random.randint(3, size=(8, 8))
    randomMatrix4 = np.random.randint(3, size=(8, 8))
    print("Result: ")
    print(matrix_mul(randomMatrix3, randomMatrix4))

    # Matrix Determinant
    print("----------------------------------------------------------")
    A = [
        [1, 2, 3, 4, 1],
        [8, 5, 6, 7, 2],
        [9, 12, 10, 11, 3],
        [13, 14, 16, 15, 4],
        [10, 8, 6, 4, 2],
    ]
    print(
        "Ex4.6, caluclate matrix determinant of random matrix:",
        matrix_determinant(randomMatrix3),
    )
    print("numpy test: ", np.linalg.det(randomMatrix3))
    print("Caluclate matrix determinant of random matrix:", matrix_determinant(A))
    print("numpy test: ", np.linalg.det(A))
