#Big 0
#////
#log2N
#n
#n^2
#n^3
#2

# bkmbt
# 01234
#
# 1       0
# 2       1
# 4       2
# 8       3
# 16      4
# 32      5
# 64      6
# 128     7
# 256     8
# 512     9
#
# 1k      10
# 2k      11
# 4k      12
# 8k      13
# 512k    19
#
# 1m      20
# 2m      21
# 1b      30
# 1t      40

# log 2 256 = 5

# 2^24 = 16m
# 2^37 = 128b
# 2^32 = 2b 1

#2^32 =

#will find x in a and returns is postion
def findItem(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

#keeps cuting in half untell the thing is found
def binarySearch(a, x):
    low = 0
    high = len(a) -1
    while high >= low:
        mid = (low + high)//2
        if a[mid] == x:
            return mid
        elif (x > a[mid]):
            low = mid+1
        else:
            high = mid-1
    return -1



a = [2,3,4,7,8,11,15,21,32,54,65,86,542]

print binarySearch(a, 8);
