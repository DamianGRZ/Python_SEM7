import numpy as np

def matrix_sum(m1, m2):
    try:
        if(len(m1[0]) == len(m2[0]) and len(m1) == len(m2)):
            return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
        else:
            raise Exception("Matrices are not of the same dimensions")
    except Exception as e:
        print ("error: " + str(e))
        return

def main():
    randomMatrix1 = np.random.randint(3, size=(128, 128))
    randomMatrix2 = np.random.randint(3, size=(127, 128))
    matrixSum = matrix_sum(randomMatrix1, randomMatrix2)
    print(matrixSum)

    randomMatrix3 = np.random.randint(3, size=(128, 128))
    randomMatrix4 = np.random.randint(3, size=(128, 128))
    matrixSum = matrix_sum(randomMatrix3, randomMatrix4)
    print(matrixSum)

if __name__ == "__main__":
    main()
