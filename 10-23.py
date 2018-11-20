#link list
class Node:
    def __init__(self, item, nxt):
        self.mItem = item
        self.mNext = nxt

class UUC:
    def __init__(self):
        self.mFirst = none

    def Insert(self, item):
        if self.Exists(item):
            return False
        n = Node(item, None)
        # n.mNext = self.mFirst
        return True

    def Exists(self, item):
        current = self.mFirst
        while current:
            if current.mItem == item:
                return True
            current = current.mNext
        return False

    def Retrieve(self, item):
        current = self.mFirst
        while current:
            if current.mItem == item:
                return current.item
            current = current.mNext
        return None

    def traverse(self, callbackFunction):
        current = self.mFirst
        while current:
            callbackFunction(current.mItem)
            current = current.mNext

    def Size(self):
        count = 0
        current = self.mFirst
        while current:
            if current.mItem == items:
                return True

    #see on line note for full notes
    #watch some youtube on link lists
    #and operator overloading
    #realy look at link list for final
    #double link list both ways
    #with 8 bits instted of 4 bits
    #can add a back pointer
