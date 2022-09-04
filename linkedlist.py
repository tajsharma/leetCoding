class Node:
    def __init__(self, dataval= None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
        


list1 = LinkedList()
list1.headval = Node(1)
j = Node(2)
k = Node(45)
l = Node("last")
list1.headval.nextval = j
j.nextval = k
k.nextval = l
l.nextval = None

list1.listprint()