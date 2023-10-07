import time
import random
from random import randint

def GenerateRandomNumbers():
    random_list = []
    howmany = int(input("How many numbers do you want to have in the list? "))
    for i in range(0, howmany):
        random_list.append(random.randint(0, 5000))
    return random_list


def bubbleSort(myList):
    moreSwaps = True
    while moreSwaps:
        moreSwaps = False
        for element in range(len(myList) -1):
            if myList[element] > myList[element + 1]:
                moreSwaps = True
                temp = myList[element]
                myList [element]= myList[element + 1]
                myList[element + 1] = temp
    return myList

def testBubbleSort():
    myList = GenerateRandomNumbers()
    print("This is the original list: ", myList)
    sortedList = bubbleSort(myList)
    theTime = str(time.perf_counter())
    print("This is the sorted list with the time: ", sortedList, theTime)

testBubbleSort()
