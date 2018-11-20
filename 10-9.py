def infixToPostFix(infix):
    s = myStack()
    postFix=""
    for c in infix:
        if c in "0123456789Xx":
            postFix+=c
        elif c in "*/":
        elif c in "+-":
        elif c in "==":
        elif c in "(":
        elif c in ")":
        else:
    #pop all on s to postfix
    return postfix

def EvalvatePostfix(postFix):
    s = Mystack()
    for c in postfix:
        if c in "0123456789Xx":
        elif c in "xX":
        elif c in =='-':
            rhs=s.pop()
            lhs=s.pop()
            resuit=lhs-rsh
            s.push(result)
        #pop and return
