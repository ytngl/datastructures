import random


def swapCompare(num1, num2):
    if num1 < num2:
        temp = num1
        num1 = num2
        num2 = temp
    return num1, num2


def bubbleSort(mainArr, arrLen):
    mainArrLen = len(mainArr) - 1
    if arrLen == 0:
        return mainArr
    for x in range(mainArrLen):
        if mainArr[mainArrLen] < mainArr[mainArrLen - 1]:
            mainArr[mainArrLen], mainArr[mainArrLen - 1] = swapCompare(mainArr[mainArrLen], mainArr[mainArrLen - 1])
        mainArrLen = mainArrLen - 1
    return bubbleSort(mainArr, arrLen - 1)


def genArray(arrLen, arrMin, arrMax):
    arrOfRanNum = []
    for x in range(arrLen):
        ranNum = random.randint(arrMin, arrMax)
        arrOfRanNum += [ranNum]
    return arrOfRanNum


def main():
    arrLen = 5
    mainArr = genArray(arrLen, 1, 1000)
    print("\n", "Main Array:\n--:w-----\n", mainArr)
    sortedArray = bubbleSort(mainArr, arrLen)
    print("\n", "Sorted Array:\n-------\n", sortedArray, "\n")


main()
