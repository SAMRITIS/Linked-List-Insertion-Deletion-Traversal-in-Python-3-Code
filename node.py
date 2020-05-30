#Create Node
class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
#Create Linked List
class Linked:
    def __init__(self):
        self.head = None
    #insert node in last element
    def insert(self, d):
        temp = self.head
        new = node(d)
        if self.head == None:

            self.head = new
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new
    # Show all element of linked list
    def show(self):
        temp = self.head
        while temp!= None:
            print(temp.data,' ', end='')
            temp = temp.next
        print(' ')
    #Delete all element from beginning
    def delete(self):
        self.head = self.head.next
    #Delete input value node
    def de(self, v):
        temp = self.head
        while temp.next.data != v :
            temp = temp.next
        temp.next = temp.next.next
    #Insert Node at Head Node
    def ins(self, da):
        new = node(da)
        new.next = self.head
        self.head = new
    def d(self):
        temp = self.head
        while temp.next.next!=None:
            temp = temp.next
        temp.next = None


print('Linked List Created')
h = Linked()
print('Insert New Node 10 at end of Linked List')
h.insert(10)
h.show()
print('Insert New Node 20 at end of Linked List')
h.insert(20)
h.show()
print('Insert New Node 30 at end of Linked List')
h.insert(30)
h.show()
print('Delete Head Node')
h.delete()
h.show()
print('Insert New Node 50 at end of Linked List')
h.insert(50)
h.show()
print('Insert New Node 40 at end of Linked List')
h.insert(40)
h.show()
print('Delete Node which value is 50')
h.de(50)
h.show()
print('Insert New Node 5 at beginning of Linked List')
h.ins(5)
h.show()
print('Delete Node From End of Linked List')
h.d()
h.show()
print('Delete Node From End of Linked List')
h.d()
h.show()