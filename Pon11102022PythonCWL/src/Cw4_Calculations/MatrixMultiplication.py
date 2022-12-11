import numpy as np

def matrix_mul(m1, m2):
    result = np.random.randint(1, size=(128, 128))  # zeros array
    if len(m1[0]) == len(m2) and len(m1) == len(m2[0]):
        for row in range(len(m1[0])):
            for col in range(len(m1)):
                for i in range(len(m2)):
                    result[row][col] += m1[row][col] * m2[i][col]
        return result
    else:
        raise Exception("Sorry, incorrect matrix dimensions")
        return

def main():
    randomMatrix1 = np.random.randint(3, size=(8, 8))
    randomMatrix2 = np.random.randint(3, size=(8, 8))
    print("Result: \n", matrix_mul(randomMatrix1, randomMatrix2))

    randomMatrix3 = np.random.randint(3, size=(7, 8))
    randomMatrix4 = np.random.randint(3, size=(8, 8))
    print("Result: \n", matrix_mul(randomMatrix3, randomMatrix4))

if __name__ == "__main__":
    main()
