import random

def sort(toSort):
    listLenght = len(toSort)
    for i in range(listLenght, 0, -1):
        for j in range(listLenght - 1, listLenght - i, -1):
            if toSort[j] > toSort[j - 1]:
                toSort[j], toSort[j - 1] = toSort[j - 1], toSort[j]
    return toSort

def main():
    randomList = random.sample(range(1, 100), 50)
    print("List before sorting:")
    print(randomList)
    print("List after sorting:")
    print(sort(randomList))
    print("List after sorting python:")
    randomList.sort(reverse=True)
    print(randomList)

if __name__ == "__main__":
    main()
