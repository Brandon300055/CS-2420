import random

#    0 1 2 3 4 5 6 7 8 9
a = [2,0,4,3,8,3,8,6,9,4]

#1st assignment do next friday
#assignments are do when they are due
#no late work!!!!!!!!!!!!!!!!!!!!!

#top down start with main and work down

#crate a list of random numbers with a scope n and a length with repeat

def CreateRandomList(n):
    A = []
    for i in range(n):
        A.append(random.randrange())
    return A

#compair every one with there nabor and swop if out of place
#keep doing swops over the list until the num of swops = 0
def BubbleSort(A):
    somethingSwithched = True
    while somethingSwithched == True:
        somethingSwithched = False
        for i in range(0, len(A)-1):
            #the switch
            if (A[i]>A[i+1]):
            #or for just python
                A[i],A[i+1]=A[i+1],A[i]
                somethingSwithched = True

#shecker sort
#the only dif is that that passes sends to the end
#for i in range (len(A)-2, -1, -1)

def Shecker(A):
    # somethingSwitched = True
    # while somethingSwithched == True:
    #     somethingSwithched = False
    #     for i in range(len(A) - 2, -1, -1):
    #         # the switch
    #         if (A[i] > A[i + 1]):
    #             # or for just python
    #             A[i], A[i + 1] = A[i + 1], A[i]
    #             somethingSwithched = True
    somethingSwitched = True
    while somethingSwitched:

        #pass to the right
        somethingSwitched = False
        for i in range(0, len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]

        #break
        if somethingSwitched == False:
            break

        #pass to the left
        somethingSwitched = False
        for i in range(len(a)-1,0,-1):
            if a[i] < a[i+1]:
                a[i], a[i-1] = a[i-1], a[i]
                somethingSwitched = True


def Selectorsort(a):
    somethingSwitched = False
    while somethingSwitched:
        for i in range(len(a)):
            smallestIndex = i

            for i in range(i+1):
                if a[i] < a[i + 1]:
                    smallestIndex = i
                    somethingSwitched = True






# main
def main():

    #for bublesort
    a = CreateRandomList(10)
    b = a[:] #<- use these to not act as a refrech but a new thingy
    BubbleSort()
    b.sort()
    if a!=b:
        print("it works");
    else:
        print("does not work!")
    #for shakerSort

print(main())

    #for selectSort
