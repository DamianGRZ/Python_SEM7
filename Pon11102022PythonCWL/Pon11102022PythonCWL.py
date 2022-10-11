import os
from pathlib import Path
from PIL import Image
import workWithFiles
import random
import inout
import math

def delete_silver_word(fullPath):
    excludedWords = "sie, oraz, i, dlaczego, nigdy"
    for path in fullPath.glob('*'):
        # check if current path is a file
        if os.path.isfile(path):
            file_extension = path.suffix
            if file_extension == ".txt":
                with open(path, 'r') as file:
                    text = file.read()
                with open('file.txt', 'w') as file:
                    for excludedWord in excludedWords:
                        # Delete
                        new_text = text.replace(excludedWord, '')
                        # Write
                        file.write(new_text)

def quadratic_equation(a, b, c):
    discriminant = pow(b, 2) - 4*a*c
    if(discriminant > 0):
        x1 = (-b-math.sqrt(discriminant)/(2*a))
        x2 = (-b+math.sqrt(discriminant))/(2*a)
        return x1, x2
    elif discriminant == 0:
        return (-b/(2*a))
    elif(discriminant < 0):
        x1 = x2 = (-b/(2*a))
        im = math.sqrt(-discriminant)/(2*a)
        return {x1, im}, {x2, im}

def sort(toSort):
    listLenght = len(toSort)
    for i in range(listLenght,0,-1):
        for j in range(listLenght-1, listLenght - i,-1):
            if (toSort[j] > toSort[j - 1]):
                toSort[j], toSort[j-1]=toSort[j-1], toSort[j]
    print(toSort)

def scalarMul(a, b):
    scalarMulsum = 0
    for index in range(0, len(a)):
        scalarMulsum = scalarMulsum + a[index] * b[index]
    return scalarMulsum

def matrix_sum(m1, m2):
    for a in m1:
        for b in m2:


if __name__ == "__main__":
    indentation = 0
    #inout.hello_world();
    #print("Files count:", workWithFiles.count_files('D:\Semestr7\Python'))
    #rec_show_trunk(Path('D:\Semestr7\Python'), indentation)
    #jpg2png(Path('D:\Semestr7\Python\jpg_files'))
    #delete_silver_word(Path('D:\Semestr7\Python\files'))
    #print(quadratic_equation(2,0,1))
    randomList = random.sample(range(1,100),50)
    print(randomList)
    sort(randomList)
    print(scalarMul([1,2,12,4], [2,4,2,8]))
    randomMatrix1 = random.sample(range(1,100),size = (128, 128))
    randomMatrix2 = random.sample(range(1,100),size = (128, 128))
    matrix_sum(randomMatrix1, randomMatrix2)

