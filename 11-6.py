#binarySearch Tree
#implements recursion
#very similar to a mix between MergeSort and

def exists(self, item):
    current = self.mRoot
    while current:
        if current.mItem == item:
            return True
        elif item < current.mItem:
            current = current.l
        else:
            current = current.r
        return Return

#the recurstions solotion
def Exists(self, item):
    return self.ExstsR(item, self.mRoot)

def ExitstsR(self,item,current):
    if current is none:
        return false
    elif current.mItem == item:
        return True
    else item < current.mItem:
        return self.Exisitr(item,current.l)
    else:
        return self.enistens(item,Current)

def Insert(self,item):
    if self.existst(item):
        return False
    self.insertR(item,self, mroot)
    return attributes

def InsertR(self,item,current):
    if currentR(self, intem, current):
        if current is none:
            current = node(item)
        elif item < current.mItem:
            self.insertR(item,current.l)
        else:
            self.InsertR(item, current.r)
#11-8

def Revrieve(self, item):
    if not self.Exxitst(item):
        return None
    return self.RetriveR(item, sel.mRoot)

def RetrieveR(self, item, current):
    if item == current.mItem:
        return current.numItems
    elif item < current.mItem:
        return self.RetrieveR(item,current.mL)
    else:
        return self.RetriveveR(item,current.mR)

def Traverse(self, callback):
    self.TraverseR(callback,self.mRoot)

def TraverseR(self,callback,current):
    if current:
        callback(current.mItem)
        self.TraverseR(callback,current.R)
        self.TraverseL(callback,current.L)

#/////
def size(self):
    count = 0
    size = self.sizeR(self.Root,count)
    return count[0]

def SizeR(self, current, count):
    if current == None:
        return
    else:
        count[0] += 1
        sizeR(current.mL,count)
        sizeR(current.mR,count)
#////best size//
def size(self):
    return self.sizeR(self.mRoot)

def sizeR(self, current):
    #base case recurtions
    if current is None:
        return 0
    return 1 + self.sizeR(current.L) + self.sizeL(current.R)



#//////
def retrieveR(self, item, current):
    if not self.Exists(current):
        return False
    elif(current.item == item):
        return none
    elif(item < current.mItem)
        return

def Retrieve(self, item):
    return self.retrieveR(item)


def traverse(self, item):
    current = item
    if not self.Exists(current):
        return False
    elif(current.item ==item):
        return current.mItem
    elif(item < current.mItem)
        return

def Traverse(self, item):
    return self.ExstsR(item)
