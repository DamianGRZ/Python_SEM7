def scalarProduct(a, b):
    try:
        if(len(a) == len(b)):
            scalarProduct = 0
            for index in range(0, len(a)):
                scalarProduct = scalarProduct + a[index] * b[index]
            return scalarProduct
        else:
            raise Exception("Matrices are not of the same length")
    except Exception as e:
        print ("error: " + str(e))
        return

def main():
    A = [1, 2, 12, 4]
    B = [2, 4, 2, 8]
    A_wrong_length = [1, 2, 12, 4, 6]
    B_wrong_length = [2, 4, 2]
    print("Correct: ")
    print("First: ", *A)
    print("Second: ", *B)
    product = scalarProduct(A, B)
    print("Scalar Product = ", product)

    print("Wrong B: ")
    print("First: ", *A)
    print("Second: ", *B_wrong_length)
    product = scalarProduct(A, B_wrong_length)
    print("Scalar Product = ", product)

    print("Wrong A: ")
    print("First: ", *A_wrong_length)
    print("Second: ", *B)
    product = scalarProduct(A_wrong_length, B)
    print("Scalar Product = ", product)

if __name__ == "__main__":
    main()
