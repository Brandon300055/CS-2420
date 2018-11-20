
#shaker sort

import random

#selection sort
#
# for i:
#     smallestindex = i
#     for i from i + 1 throght end
#       reset as needed smallest index
#       swit A[i] and A[smallestindex]

#merge short


#quicksort


def CreateRandomListWithoutDuplicates(n):
    A = []
    for i in range(n):
        A.append(i)
    for i in range(n):
        j = random.range(0,n)
        A[i], A[j] = A[j], A[i]


    # A = []
    # i=0
    # while i < n:
    #     r = random.rangerange(0,n)
    #     if r not in A:
    #         A.append(r)
    #         i += 1
    # return A