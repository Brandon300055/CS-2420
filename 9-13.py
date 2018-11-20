def countingSort(A):
    #int f arrays

    #loop over a, counting into fail

    #loop over F, refilling A

#web3400.jacefugate.com/power_of_two

#hash sort has the best big
    def MergeSort(self, A):
        #base case
        if len(A)<=1:
            return
        #break into l and r
        L = A[:int(len(A)/2)]
        R = A[int(len(A)/2):]

        #magicly sort thorgh recursion
        self.MergeSort(L)
        self.MergeSort(R)

        #do the join
        B = []

        #while something left in l and r pick the smallest of the 2 and move it into A
        while ((len(L) + len(L))) > 1:

            if (min(L) < min(R)):
                B.append(min(L))
                L.pop(L.index(min(L)))

            else:
                B.append(min(R))
                R.pop(R.index(min(R)))

            #while there is no longer anythhing left in L move R into A
            while (len(L) == 0):
                if (len(R) == 0):
                    B + B
                    break
                else:
                    B.append(min(R))
                    R.pop(R.index(min(R)))


            #while there is no longer anythhing left in R move L into A
            while (len(R) == 0):
                if (len(L) == 0):
                    B + B
                    break
                else:
                    B.append(min(L))
                    L.pop(L.index(min(L)))

        A = B
        return A
