from graphics import *
import math

def main():
    PrintInstructions()
    infix = input("Your Formula")
    postfix = InfixToPostfix()
    win = GraphWin("My Circle", 500, 500)
    xlow = -10
    ylow = -10
    xhigh = 10
    yhigh = 10
    xinc = .1

    win.setCoords(xlow, ylow, xhigh, yhigh)
    p2 = None
    x = xlow
    while x < xhigh:
        y = (int(x)-2)*(int(x)+1)(int(x)+3))
        p = Point(x,y)
        if p2:
            ln = Lin(p, p2)
            ln.draw(win)
        p2 = p
        x+= .1
    win.getMouse()
    win.close()
main()


##infix / post fix or revers polish notation rpn
def InfixToPostfix(infix):
    postfix = ""
    stack = ""
    for i in infix:
        print(i)
    #make
    #(1234+123465)*(123+12)
    #1234 123465 + 123 12 + *
    #never change the order of the operatans just the operators

    pass
