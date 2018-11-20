#This programe solves the towers of hanoi for N disks useing recursion

def move(N, f, t, o):
    if N <=1:
        print("Move 1 Disk from tower", f, "to tower", t)
    else:
        move(N-1, f, o, t)
        move(1, f, t, o)
        move(N-1, o, t, f)


def main():
    N = 4
    move(N, 1, 2 ,3)



main()
