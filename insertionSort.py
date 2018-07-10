import random


def insertionSort(mainArr):
    for i in range(0, len(mainArr)):
        currentVal = mainArr[i]
        currentPos = i

        while currentPos > 0 and mainArr[currentPos - 1] > currentVal:
            mainArr[currentPos] = mainArr[currentPos - 1]
            currentPos = currentPos - 1

        mainArr[currentPos] = currentVal


def genArray(arrLen, arrMin, arrMax):
    arrOfRanNum = []
    for x in range(arrLen):
        ranNum = random.randint(arrMin, arrMax)
        arrOfRanNum += [ranNum]
    return arrOfRanNum


def main():
    mainArr = genArray(9, 1, 1000)
    print("\n", "Main Array:\n--------\n", mainArr)

    insertionSort(mainArr)
    print("\n", "Sorted Array:\n-------\n", mainArr, "\n")


main()
