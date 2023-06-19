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

    def OddEvenLL(self,head):
        if not head:
            return head


        odd = head
        even = head.nextval
        e_head = even

        while even and even.nextval:
            odd.nextval = odd.nextval.nextval
            odd = odd.nextval
            even.nextval = even.nextval.nextval
            even = even.nextval

        odd.nextval = e_head

        return head
        



#need to fix this class ***
    def hasCycle(self, head):
        hashSet = {}

        while head:
            if head in hashSet: return True
            hashSet[head]=True
            head=head.next
        return False

#intitializes a linked list with a cycle 
list1 = LinkedList()
list1.headval = Node(1)
one = Node(2)
two = Node(45)
three = Node(99)
four = Node(12)
five = Node(63)
list1.headval.nextval = one
one.nextval = two
two.nextval = three
three.nextval = four
four.nextval = five
five.nextval = None



newhead = list1.OddEvenLL(list1.headval)
print(newhead.dataval)

