def infixToPostFix:
    :
    :
    if c in "+-":
        while not s.Empty() and s.top() in "+-*/":
            Postfix += s.pop()
        s.push(c)
        if c ==')':
            while s.top() !='(':

#link list for uuc ADT (ON the Test)
#stored in ram with a 4 bit pointer and where the next one is

#can jump around the ram  and can fill fragmented memory

#memory . insert and delte, maintaining order with out moving items

#it is none ordered

#is the first page       points the first mItem
#self.mFirst             #Item

class Node:
    def __init__(self):
        self.mItem = item
        self.mNext = nxt


class UUC:
    def __init__(self):
        self.mFirst = None

    #creates an new instace of node and insters into it
    def Insert(self, Item):
        if self.Exists(item):
            return False
        n = Node(item, None)
        n.mNext = self.mFirst
        self.mFirst = n
        return True

    def Exists(self, item):
        current = self.mFirst
        while current: != None:
            if current.mItem == item:
                return True
            current = current.mNext
        return False





#look into the hungaryan notation

#BST
