print("compareisons on random data")
sorts = [Bubble, Shaker]

print("          ," end="")
for sort in sorts:
        #              echo sorts    do no end with return
    print ("%10s" % (sort.__name__), end = "")
print()
for size in range(3, 13):
    numItems = 2 ** size
    print("%10i" % (size) end="")
    for sort in sorts:
        A =  CreateRandomList(numItems)
        C = Counter()
        sort(A,C)
        print("%10.2f" % (math.log2(C.compares)), end="")
    print();


#time
import time
def main():
    T1 = time.time()

    #file reading
    file = open("InsertNames.txt",r)
    studentList = []
    for line in fin:
        words = line.split()
        s=student=(word[0])

        repeat = False
        #loop and check
        if repeat is False

    fin.close()

    #some nonscencessdfasd


    T2 = time.time()
    print( T2-T1)
