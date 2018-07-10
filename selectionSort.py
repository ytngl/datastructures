import random


def genArray(arrLen, arrMin, arrMax):
    arr = []
    for x in range(arrLen):
        ranNum = random.randint(arrMin, arrMax)
        arr += [ranNum]
    return arr


def selectionSort(arr, arrLen):
    index = 0
    minVal = arr[index]
    if arrLen == 0:
        return arr
    for x in range(arrLen):
        if minVal > arr[index]:
            minVal = arr[index]
        index = index + 1
    arr = arr + [arr.pop(arr.index(minVal))]
    return(selectionSort(arr, arrLen - 1))


def main():
    arrLen = 5
    mainArr = genArray(arrLen, 1, 100)
    print("\n", "Main Array:\n-------\n", mainArr)
    sortedArray = selectionSort(mainArr, arrLen)
    print("\n", "Sorted Array:\n-------\n", sortedArray)


main()
