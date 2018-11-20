# gTotalAge =0

def AddAge(s, c):
    # global gTotalAge
    # gTotalAge += S.GetAge()
    c.Add(s.GetAge())


def main():
    global gTotalAge
    Allstudents = bst.UUC()
    #insert


    #average
    c = Counter()
    Allstudents.Traverse(AddAge, c)
    print (c.GetInterger / AllStudents.Size())

    #delete


    #retrieve

#BST NOTes
#last row is full #23 tree
#complete is going left to right is not missing any utill it stops
#balanced is having as many on the left as on the right #avl

#extra crited
#build a 23 tree with the following methods
#20
    #insert
    #traverse
    #retrivece
    #delete #30

    #total: 50 points


    #delete

    # 1 replace with in order scessor if necessary
    # 2 remove leaf item if still something there you are done
    # 3 try to barrow from a sibling if successful you are done
    # 4 if you cant barrow from a sibling demote parent into sibling
    # 5 unless the parent had only one item it in it and you demote the sibling then it levels a hole
    #   if that lears a hole at the parent then repeat and it is solved
