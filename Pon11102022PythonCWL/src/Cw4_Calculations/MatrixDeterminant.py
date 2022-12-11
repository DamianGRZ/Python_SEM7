import numpy as np

def sub_matrix(matrix, row, column):
    sub_matrix = matrix[:]
    sub_matrix = np.delete(sub_matrix, 0, axis=0)  # Delete row
    sub_matrix = np.delete(sub_matrix, column, axis = 1) #delete column
    return sub_matrix

def matrix_determinant(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    if(num_rows != num_cols):
        raise Exception("Not a square matrix")
        return
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    else:
        det = 0
        for col in range(num_cols):
            sign = (-1) ** (0 + col)
            det += sign * matrix[0][col] * matrix_determinant(sub_matrix(matrix, 0, col))

    return det

def main():
    randomMatrix3 = np.random.randint(3, size=(8, 8))
    print("My function : ", matrix_determinant(randomMatrix3))
    print("Python function : ", np.linalg.det(randomMatrix3))

if __name__ == "__main__":
    main()