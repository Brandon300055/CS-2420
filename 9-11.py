def QuickSort(A, low, high, mod):
    if high - low <= 0:
        return
    #pivot = low
    if mod:
        return
    else:
        mid = (low+)


    lmgt = low + 1
    for i in range(low + high + 1):
        if A[i] < A[low]:
            #A[pivot] <= A[lmgt]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1

    pivot = lmgt - 1
    A[low], A[pivot] = A[pivot], A[low]

    QuickSort(A, low, pivot-1):
    QuickSort(A, pivot+1, high):

A = [3,1,4,1,5,9,2,6,5,3,5,4]

QuickSort(A, 0, len(A-1)):




def QuickSortReviwe(A, low, high):
    #bace case
    if high - low <= 0:
        return
    #one pass from lowest thorgh high

#left moust something
    pivot = low
    lmgt = low + 1

    #low plus 1 plus high
    for i in range(low+1,high+1):
        if A[i] < A[low]:
            A[i], A[lmgt] = A[lmgt], A[i]

    #recursen
    def QuickSortReviwe(A, low, pivot+1):
