import random
import math
import sys
#sorting algeritimes by brandon starts

class Sorting:
    def __init__(self):
        #lenth is the length of the for testing list defult is 16
        self.length = 16
        #colors
        self.SUCCESS = '\033[92m'
        self.DANGER  = '\033[91m'
        self.WARNING = '\033[93m'
        self.INFO    = '\033[94m'
        self.BOLD    = '\033[1m'
        self.ENDC    = '\033[0m'
        #emty list for sorted list
        self.sortedA = []
        #storing number of compares and swapes of the algeritimes being tested
        self.compares = 1
        self.swipe = 1


    # generate a random list
    def CreateRandomList(self, length):
        A = []
        for i in range(length):
            A.append(random.randrange(0, length))
        return A

    def CreateMostlySortedList(self, nums):
        nums = self.CountSort(nums)
        self.compares = 1
        self.swipe = 1
        nums[0], nums[len(nums)-1] = nums[len(nums)-1], nums[0]
        return nums


    #bublesort
    def BubbleSort(self, A):
        somethingSwitched = True
        while somethingSwitched == True:
            somethingSwitched = False

            #keep doing passes
            for i in range(0, len(A) - 1):
                # the switch
                self.compares+=1
                if (A[i] > A[i + 1]):
                    # switch only in python
                    A[i], A[i + 1] = A[i + 1], A[i]
                    self.swipe+=1
                    somethingSwitched = True

    # shakerSort
    def ShakerSort(self, A):
        somethingSwitched = True
        while somethingSwitched == True:
            somethingSwitched = False

            #pass to the right
            for i in range(0, len(A)-1):
                self.compares+=1
                if (A[i] > A[i + 1]):
                    self.swipe+=1
                    A[i], A[i + 1] = A[i + 1], A[i]

            #pass to the left
            for i in range(len(A)-1,0,-1):
                self.compares+=1
                if (A[i] < A[i - 1]):
                    self.swipe+=1
                    A[i], A[i - 1] = A[i - 1], A[i]
                    somethingSwitched = True

    #selectSort
    def SelectSort(self, A):
        #do as many iterations as lenth of a
        for count in range(len(A)):
            indexOfSmallestNumber = 0
            smallestNumber = 999999

            #the pass to the right
            for i in range(count, len(A)):
                self.compares+=1
                if (A[i] < smallestNumber):
                    indexOfSmallestNumber = i
                    smallestNumber = A[i]


            #set smallest numbers to index count
            self.swipe+=1
            A[count], A[indexOfSmallestNumber] = A[indexOfSmallestNumber], A[count]
            # somethingSwitched == True


    def MergeSort(self, A):
        self.compares+=1
        if len(A)>1:
            mid = len(A)//2
            lefthalf = A[:mid]
            righthalf = A[mid:]
            self.swipe+=len(A)

            self.MergeSort(lefthalf)
            self.MergeSort(righthalf)

            i=0
            j=0
            k=0
            while i < len(lefthalf) and j < len(righthalf):
                self.compares+=1
                self.compares+=1
                if lefthalf[i] < righthalf[j]:
                    self.swipe+=1
                    A[k]=lefthalf[i]
                    i+=1
                else:
                    self.swipe+=1
                    A[k]=righthalf[j]
                    j+=1
                k+=1

            while i < len(lefthalf):
                self.swipe+=1
                A[k]=lefthalf[i]
                i+=1
                k+=1

            while j < len(righthalf):
                self.swipe+=1
                A[k]=righthalf[j]
                j+=1
                k+=1

    def QuickSort(self, A):
        less = []
        equal = []
        greater = []

        self.compares+=1
        if len(A) > 1:
            pivot = A[0]
            for x in A:
                self.compares+=1
                if x < pivot:
                    less.append(x)
                    self.swipe+=1
                self.compares+=1
                if x == pivot:
                    equal.append(x)
                    self.swipe+=1
                self.compares+=1
                if x > pivot:
                    greater.append(x)
                    self.swipe+=1
        # Don't forget to return something!
            return self.QuickSort(less)+equal+self.QuickSort(greater)
        else:
            return A


    def ModQuickShort(self, A):
        return self.QuickSort(A)

    def CountSort(self, A):
        maximum = max(A)
        minimum = min(A)
        count_array = [0]*(maximum-minimum+1)

        for val in A:
            count_array[val-minimum] += 1

            sorted_array = []
            self.compares+=1
            for i in range(minimum, maximum+1):
                if count_array[i-minimum] > 0:
                    self.swipe+=1
                    for j in range(0, count_array[i-minimum]):
                        sorted_array.append(i)
        return sorted_array

    def Check(self, testArray):
        if testArray == self.sortedA:
            return self.SUCCESS + self.BOLD + " works! " + self.ENDC + str(testArray) + self.ENDC
        else:
            return self.DANGER + " does not work! " + str(testArray) + self.ENDC

    def spaces(self, n):
        #this function prints n number of spaces
        for i in range(n):
            print (" ", end = "")
        return ""

    #function list
    F = [
        BubbleSort, ShakerSort, SelectSort, MergeSort,
        QuickSort, ModQuickShort, CountSort
        ]

    def Chart(self, mostlySorted, swapesOrCompare):
        print(self.BOLD + "random data in log base 2:" + self.ENDC)
        self.spaces(10)
        for sort in self.F:
            #number of spaces - lenth of name of sorting alg            echo sorts    do no end with return
            print (self.INFO + str(sort.__name__) + self.ENDC, end = "")
            self.spaces(20 - len(sort.__name__)) # <- the spaces
        print() #return
        #build the table
        for size in range(3, 13):
            #left most col
             numItems = 2 ** size
             print(self.INFO + str(size) + self.ENDC, end="")
             self.spaces(10 - len(str(size)))

             for call in self.F:
                 #create new random list
                 list = self.CreateRandomList(numItems)
                 if (mostlySorted == True):
                     list = self.CreateMostlySortedList(list)

                 #call method
                 call(self, list)

                 if (swapesOrCompare == 1):
                     checks = self.compares
                 elif (swapesOrCompare == 0):
                     checks = self.swipe

                 total = round(math.log2(checks), 4)
                 print(total, end="")
                 self.spaces((20 - len(sort.__name__)) + len(sort.__name__) - len(str(total)) )
                 #rest self.compares
                 self.compares = 1
                 self.swipe = 1
             print()
        return ""

    def Test(self, length):
        #this method test all 7 sort methods a lists whos lenght is a given paramiter
        randomList = self.CreateRandomList(self.length)
        #sort a list for testing and comparison
        self.sortedA = randomList[:]
        self.sortedA.sort()
        #print Random Data
        print(self.BOLD + self.INFO + "Random Data: " + self.ENDC + self.BOLD + str(randomList) + self.ENDC)
        #loop over f
        for i in range(len(self.F)):
            list = randomList[:]
            #case if funtion is non returning
            newList = self.F[i](self, list)
            if (not newList is None):
                list = newList
            print (self.BOLD + self.INFO + self.F[i].__name__ + ":" + self.ENDC + self.Check(list), end="")
            print(self.INFO + " Operations: " + self.ENDC + str(math.log2(self.compares)))
            #rest self.compares
            self.compares = 1
        return ""

    def formatMenu(self):
        return [ 'What would you like to do?', '[T] Test All Functions', '[CU] Check comparisons with unsorted data', '[SU] Check swapes with unsorted data','[CS] Check comparisons with sorted data', '[SS] Check swapes with sorted data', '[Q] Quit' ]

    def getUserChoice(self, inputs):
	    inp = input(inputs)
	    inp = inp.strip()
	    while inp == "":
	    	inp = input(inputs)
	    	inp = inp.strip()
	    return inp

    def getUserFloat(self, inputs):
        while True:
            try:
                inp = float(input(inputs).strip())
                if inp > 0:
                   return inp
            except:
    	        print("You must enter a number")

    def quitAction(self):
    	print ("Have a nifty day!")
    	sys.exit( 0 )

    def applyAction(self, check):
        #run test
        if (check == "T" or check == "t"):
            num = self.getUserFloat("How long sould the random test list be?: ")
            print(self.Test(num))
        #run comparisons / swape
        elif check == "CU" or check == "cu":
            return self.Chart(False, 1)
        elif check == "SU" or check == "su":
            return self.Chart(False, 1)
        elif check == "CS" or check == "cs":
            return self.Chart(True, 0)
        elif check == "SS" or check == "ss":
            return self.Chart(True, 0)

        elif check == "Q" or check == "q":
            return self.quitAction()

    # main
    def Main(self):
        #set max setrecursionlimit
        sys.setrecursionlimit(5000)

        while True:
            menu = self.formatMenu()
		    # input = formatMenuPrompt()
		    # input = input.strip()
            for i in menu:
                print (i)
            #get user string
            check = self.getUserChoice("What would you like to do? ")
            self.applyAction(check)

        #print(self.Chart(False, 1))

#creat a new instace of main
sort = Sorting()
#call Main
sort.Main()
