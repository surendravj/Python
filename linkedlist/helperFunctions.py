# helper functions used in linked list

# Creating node


class node:
    def __init__(self, data):
        self.data = data
        self.next = None


# creating linkedList

class linkedList:
    def __init__(self):
        self.head = None

    # ----------------insertion operations on linkedList------------------------------------

    # method to insert newNode at head position

    def insertAtHead(self, newnode):
        temp = self.head
        self.head = newnode
        self.head.next = temp

    # method to insert newnode at given postions

    def insertAtPostion(self, newnode, pos):
        currentnode = self.head
        currentpostion = 0
        previousnode = None
        if(pos < 0 or pos >= self.listLength()):
            print("Invalid postion to insert value")
            return
        if(pos == 0):
            self.insertAtHead(newnode)
            return
        while(currentpostion != pos):
            previousnode = currentnode
            currentnode = currentnode.next
            currentpostion += 1
        previousnode.next = newnode
        newnode.next = currentnode

    # method to insert a newnode at tail of a linkedList

    def insertAtTail(self, newnode):
        currentnode = self.head
        if(currentnode == None):
            self.head = newnode
            return
        while(currentnode.next != None):
            currentnode = currentnode.next
        currentnode.next = newnode

    # --------------------------Deletion operations on the linkedList------------------------

    # method to delete head node from linked list

    def deleteAtHead(self):
        currentnode = self.head
        self.head = currentnode.next
        del currentnode

    # method to delete desired node by giving postion number

    def deleteAtPostion(self, pos):
        currentpostion = 0
        previousnode = None
        currentnode = self.head
        if(pos < 0 or pos > self.listLength()):
            print("Invalid postion to delete")
            return
        if(pos == 0):
            self.deleteAtHead()
            return
        elif(pos == self.listLength()):
            self.deleteAtTail()
            return
        while(currentpostion != pos):
            previousnode = currentnode
            currentnode = currentnode.next
            currentpostion += 1
        previousnode.next = currentnode.next
        del currentnode

    # method to delete tail node in a linkedList

    def deleteAtTail(self):
        currentnode = self.head
        previousnode = None
        while(currentnode.next != None):
            previousnode = currentnode
            currentnode = currentnode.next
        previousnode.next = None
        del currentnode

    # Helper functions that applied or used in the linked list

    # method to get the size of an linkedList

    def listLength(self):
        length = 0
        currentnode = self.head
        while(currentnode != None):
            length += 1
            currentnode = currentnode.next
        return length

    # method to find an element in a linkedList

    def searchElement(self, element):
        currentnode = self.head
        index = 0
        noMatch = True
        while(currentnode != None):
            index += 1
            if(currentnode.data == element):
                print(f"{element} found at node location {index}")
                noMatch = False
                return
            currentnode = currentnode.next
        if(noMatch):
            print(f"{element} is not found in the following linked list")

    # method to print the whole linkedList

    def printList(self):
        currentnode = self.head
        if(currentnode == None):
            print("List is empty")
            return
        while(currentnode != None):
            print(currentnode.data)
            currentnode = currentnode.next


linked = linkedList()

linked.insertAtTail(node("surendra"))
linked.insertAtTail(node("mani"))
linked.insertAtHead(node("satanaraya"))
linked.insertAtPostion(node("lakshmi"), 2)
linked.searchElement("mani")
linked.printList()
linked.deleteAtHead()
linked.deleteAtTail()
linked.deleteAtPostion(2)
linked.printList()
