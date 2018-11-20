import graphics
import math

#converts a string form an infix form to a post fix form
def infixToPostfix(infixexpr):
    prec = {}
    items = []
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    postfixList = []
    tokenList = list(infixexpr)

    for token in tokenList:
        if token in token in "0123456789x":
            postfixList.append(token)
        elif token == '(':
            items.insert(0,token)
        elif token == ')':
            topToken = items.pop(0)
            while topToken != '(':
                postfixList.append(topToken)
                topToken = items.pop(0)
        else:
            while (not items == []) and \
               (prec[items[0]] >= prec[token]):
                  postfixList.append(items.pop(0))
            items.insert(0,token)

    while not items == []:
        postfixList.append(items.pop(0))
    return " ".join(postfixList)

#evalutates a postfix expretion
def eval_postfix(text, x):
    s = []
    for symbol in text:
        if symbol in "0123456789":
            s.append(int(symbol))
            plus = None
        elif symbol == "x":
            s.append(int(x))
            plus = None
        elif len(s) != 0:
            if symbol == "+":
                plus = s.pop() + s.pop()
            elif symbol == "-":
                plus = s.pop() - s.pop()
            elif symbol == "*":
                plus = s.pop() * s.pop()
            elif symbol == "/":
                plus = s.pop() / s.pop()
        if plus is not None:
            s.append(plus)
    return int(plus)

#graphics an inputed equation
def main():
    infix = input("y=")
    postfix = infixToPostfix(str(infix))
    print(postfix)
    win = graphics.GraphWin("Graphicing Calculator", 500, 500)
    xlow = -100
    ylow = -100
    xhigh = 100
    yhigh = 100
    xinc = .1

    win.setCoords(xlow, ylow, xhigh, yhigh)
    p2 = None
    x = xlow
    while x < xhigh:
        y = eval_postfix(str(postfix), int(x))
        #
        p = graphics.Point(x,y)
        if p2:
            ln = graphics.Line(p, p2)
            ln.draw(win)
        p2 = p
        x+= .1
    win.getMouse()
    win.close()

print(main())
