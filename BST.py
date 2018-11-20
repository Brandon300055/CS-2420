#binarySearch tree
#by Brandon Stewart

class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    #insert a new node
    def Insert(self, data):
        #is the same value
        if self.value == data:
            return False
        #is bigger and return the right node
        elif self.value > data:
            #if already exists return insert
            if self.leftChild:
                return self.leftChild.Insert(data)
            else:
                self.leftChild = Node(data)
                return True
        #is bigger and return the right node
        else:
            #if already exists return insert
            if self.rightChild:
                #assign the new child node
                return self.rightChild.Insert(data)
            else:
                #assign the new child node
                self.rightChild = Node(data)
                return True

    def Exists(self, data):
        #if it is the value you are looking for
        if (self.value == data):
            return True
        #elif it is bigger go down the left node
        elif self.value > data:
            #if there is a left node
            if self.leftChild:
                #recurs and go down that node
                return self.leftChild.Exists(data)
            else:
                return False
        else:
            if self.rightChild:
                self.rightChild.Exists(data)
            else:
                return False

    def Traverse(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.Traverse()

            if self.rightChild:
                self.rightChild.Traverse()


    # def Traverse(self, callback):
    #     return self.TraverseR(callback, self.value)
    #
    # def TraverseR(self, cb, node):
    #     if node is node:
    #         return None
    #     self.TraverseR(cb, node.leftChild)
    #     print(cb(node.value))
    #     self.TraverseR(cb, node.rightChild)

    # def Traverse(self, callback):
    #     return self.TraverseR(callback, self.value)

class BST():
    def __init__(self):
        self.root = None
    def Insert(self, data):
        if self.root:
            #return
            return self.root.Insert(data)
        else:
            #create a new node
            self.root = Node(data)
            return True

    def Exists(self, data):
        if self.root:
            return self.root.Exists(data)
        else:
            return False

    def AddAges(self):
        return 10

    def Traverse(self):
        return self.root.Traverse()
        # return self.root.Traverse(self.AddAges())

    def Delete(self):
        pass
    def Retrieve(self):
        pass
    def Size(self):
        pass


bst = BST()
bst.Insert(10)
bst.Insert(11)
bst.Insert(12)
bst.Insert(13)
bst.Insert(14)
print(bst.Traverse())
print(bst.Exists(12))

class Main:

    def __init__(self, arg):
        self.arg = arg

    def Main():
        pass


# class ContainerBST():
#     def __init__(self):
#         this.kittens = 0
#
#     def CallBST(self):
