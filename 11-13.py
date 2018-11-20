def delete(self, item):
    if not self.exists(item):
        return False
    self.DeleteR(item, self.mroot)
    return True

def delete(self, item):
    if item < current.mItem:
        self.DeleteR(iTem,current.l)
    elif item > current.mItem:
        self.deleteR(iTem, current.r)
    else: #delete item in current
        if current.L is None and Current.R is None:
            current = None
        elif current.R is None:
            current = current.L
        elif current.l is None:
            current = current.R
        else: #Two Children
        #find in order successor
        z = current.r
        while Z.l:
            z=Z.l
        current.mItem = Z.mItem
        current.r=self.deleteR(z.mItem,current.r)
        return current

    def main():
        AllStudents = bst.uuc()
        fin open("insertNameMedium.txt", "r")
        for lin in fin:
            words = line.splits()
            newStudent = student(words[0])
            ok = Allstudents.Insert(newstudent)
            if not ok:
                print
