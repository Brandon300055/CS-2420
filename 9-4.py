#notes

#recursion
def factorial(N):
    if N <= 1:
        return 1
    else:
        return N * factorial(N-1)

print(factorial(5))

#towers of Hanoi
