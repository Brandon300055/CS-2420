#find a solution for the 8-queens problem

def PlaceQueen(cols, c):
    if c == 8:
        print("Found a solution!, cols")
        return
    for r in range(8)
    cols[c] = r 

def main():
    cols = [-1] * 8
    PlaceQueen(cols, 0)
