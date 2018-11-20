import time
import sys

class Student:
    def __init__(self, file):
        self.insertList = self.read(file)
        self.retrieveList = []
        self.SUCCESS = '\033[92m'
        self.DANGER  = '\033[91m'
        self.WARNING = '\033[93m'
        self.INFO    = '\033[94m'
        self.BOLD    = '\033[1m'
        self.ENDC    = '\033[0m'

    # def read(self):
    def read(self, file):
        #
        list = []
        fileContent = open(file)
        #break down by line
        for line in fileContent:
            #break down by word
            line = line.split()
            list.append(line)

        return list
            #print(line)
            #do check
            # self.ssnList.append(ssn)

    #this method checks for duplicates
    # def goOver(self, delete, lists):
    #     if delete == 1:
    #         list == lists
    #     else:
    #         list = []
    #
    #     for ssn in self.insertList:
    #         repeat = False
    #         for ssns in list:
    #             if ssns == ssn[2]:
    #                 repeat = True
    #         if repeat == False:
    #             if delete == 0:
    #                 list.append(ssn[2])
    #             print(ssn[2])
    #         else:
    #             if delete == 0:
    #                 for i in range(100):
    #                     print("error duplicate")
    #             else:
    #                 self.insertList.append(ssn[2])
    #                 for i in range(100):
    #                     print("item remove")
        # list = []
        # for ssn in self.insertList:
        #     repeat = False
        #     for ssns in lists:
        #         if ssns == ssn:
        #             repeat = True
        #             #for i in range(10):
        #             print("error duplicate")
        #     if repeat == False:
        #         list.append(ssn)
        #         print(ssn)

    #this method will look for duplicates
    def duplicate(self):
        t1 = time.time()
        list = []
        for ssn in self.insertList:
            repeat = False
            for ssns in list:
                if ssns == ssn[2]:
                    repeat = True
            if repeat == False:
                list.append(ssn[2])
                print(ssn[2])
            else:
                for i in range(100):
                    print("error duplicate " + str(ssn[2]))
        t2 = time.time()
        return (self.INFO + str(t2-t1) + self.ENDC)

    #this method will delete specified recoreds in the file provided
    def delete(self, file):
        t1 = time.time()
        list = self.read(file)
        newList = []
        for ssn in self.insertList:
            repeat = False
            for ssns in list:
                if ssns[0] == ssn[2]:
                    repeat = True
            if repeat == False:
                #add to new list
                newList.append(ssn)
                print (ssn[2])
            else:
                print("Record Deleted " + str(ssn[2]))
        self.insertList = newList
        t2 = time.time()
        return (self.INFO + str(t2-t1) + self.ENDC)

    #this method will get the average age of insertList
    def traverse(self):
        t1 = time.time()
        age = 0
        count = 0
        for line in self.insertList:
            age += int(line[4])
            count += 1
        print(self.SUCCESS + str(age/count) + self.ENDC)
        t2 = time.time()
        return (self.INFO + str(t2-t1) + self.ENDC)

    #this method will get the average age of the users provided
    def retrieve(self, file):
        t1 = time.time()
        list = []
        age = 0
        count = 0

        #call read method for file save it to traverseList
        self.retrieveList = self.read(file)
        for line in self.insertList:
            repeat = False
            for ssn in self.retrieveList:
                #print(ssn)
                if ssn[0] == line[2]:
                    age += int(line[4])
                    count += 1
        print(self.SUCCESS + str(age/count) + self.ENDC)
        t2 = time.time()
        return (self.INFO + str(t2-t1) + self.ENDC)
            #     if
    def formatMenu(self):
        return [ self.BOLD + self.WARNING +'What would you like to do?' + self.ENDC, 'Check for duplicates [D] ', 'Traverse the list [T] ', 'Retrieve from RetrieveNames.txt [R] ','Delete from DeleteNames.txt [DEL] ', '[Q] Quit' ]

    def getUserChoice(self, inputs):
	    inp = input(inputs)
	    inp = inp.strip()
	    while inp == "":
	    	inp = input(inputs)
	    	inp = inp.strip()
	    return inp

    def quitAction(self):
    	print ("Have a nifty day!")
    	sys.exit( 0 )

    def applyAction(self, check):
        #run test
        if (check == "D" or check == "d"):
            print(self.duplicate())
        elif check == "t" or check == "t":
            return self.traverse()
        elif check == "R" or check == "r":
            return self.retrieve("RetrieveNames.txt")
        elif check == "DEL" or check == "del":
            return self.delete("DeleteNames.txt")
        elif check == "Q" or check == "q":
            return self.quitAction()

    def main(self):
        while True:
            #get menu
            menu = self.formatMenu()
            for i in menu:
                print (i)
            #get user string
            check = self.getUserChoice("What would you like to do? ")
            print(self.applyAction(check))


student = Student("insertnames.txt")
print(student.main())


    # def main():
    #     studentList = []
    #     #Inserting
    #     fin = open("insertnames.txt")
    #     for lin in fin:
    #         words = line.split()
    #         s = student(words[,],words[,]...)
    #         repeat = False
    #         #for previous student in student list
    #         for s2 in student(i):
    #             if s2.massn == s.massn
    #                 print("")
    #                 repeat = True
    #             if not repeat:
    #             studentList.append(s)
    #         fin.close()
    #         t2=Time.Time()
    #         print(....t2-t1)
