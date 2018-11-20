import random
#sorting algeritimes by brandon starts

# generate a random list
def CreateRandomList(n):
    A = []
    for i in range(n):
        A.append(random.randrange(0,n))
    return A


def BubbleSort(A):
    somethingSwitched = True
    while somethingSwitched == True:
        somethingSwitched = False

        #keep doing passes
        for i in range(0, len(A) - 1):
            # the switch
            if (A[i] > A[i + 1]):
                # switch only in python
                A[i], A[i + 1] = A[i + 1], A[i]
                somethingSwitched = True

# shakerSort
def ShakerSort(A):
    somethingSwitched = True
    while somethingSwitched == True:
        somethingSwitched = False

        #pass to the right
        for i in range(0, len(A)-1):
            if (A[i] > A[i + 1]):
                A[i], A[i + 1] = A[i + 1], A[i]

        #pass to the left
        for i in range(len(A)-1,0,-1):
            if (A[i] < A[i - 1]):
                A[i], A[i - 1] = A[i - 1], A[i]
                somethingSwitched = True



#selectSort
def SelectSort(A):
    #do as many iterations as lenth of a
    for count in range(len(A)):
        indexOfSmallestNumber = 0
        smallestNumber = 999999

        #the pass to the right
        for i in range(count, len(A)):
            if (A[i] < smallestNumber):
                indexOfSmallestNumber = i
                smallestNumber = A[i]


        #set smallest numbers to index count
        A[count], A[indexOfSmallestNumber] = A[indexOfSmallestNumber], A[count]
            # somethingSwitched == True


def check(testArray, sortedString):
    SUCCESS = '\033[92m'
    DANGER  = '\033[91m'
    ENDC    = '\033[0m'
    if testArray == sortedString:
        return SUCCESS + " works " + str(testArray) + ENDC
    else:
        return DANGER + " does not work! " + str(testArray) + ENDC


# main
def main():
    INFO    = '\033[94m'
    SUCCESS = '\033[92m'
    BOLD    = '\033[1m'
    ENDC    = '\033[0m'

    # for bublesort
    A = CreateRandomList(10)
    #use these to act as a create new arrays
    sortedString = A[:]
    bubleArray = A[:]
    shakerArray = A[:]
    selectArray= A[:]

    #sort sortedString for testing and comparison
    sortedString.sort()

    #print Original for refrechs
    print(INFO + "The Original: " + ENDC + BOLD + str(A) + ENDC)

    #call BubbleSort
    BubbleSort(bubleArray)
    #check BubbleSort
    print (INFO + "BubbleSort" + ENDC + check(bubleArray, sortedString))

    #call ShakerSort
    ShakerSort(shakerArray)
    #check ShakerSort
    print (INFO + "ShakerSort" + ENDC + check(shakerArray, sortedString))
    
    #call ShakerSort
    SelectSort(selectArray)
    #check ShakerSort
    print (INFO + "SelectSort" + ENDC + check(selectArray, sortedString))





print(main())
