# single linked list implementaion in python and also
# implementaion of helper function used in linked list


# Creating Node

class node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Creating linkedList


class linkedList:
    def __init__(self):
        self.head = None

    # ----------------------------insertion operations on linkedList----------------------------------------

    # Method to insert a node at head postion

    def insertAtHead(self, newnode):
        current_node = self.head
        if(current_node == None):
            self.head = newnode
            return
        self.head = newnode
        self.head.next = current_node

    # Method  to insert newnode at end of the list

    def insertAtEnd(self, newnode):
        current_node = self.head
        if(current_node == None):
            self.head = newnode
            return
        while(current_node.next != None):
            current_node = current_node.next
        current_node.next = newnode

    # Method to insert newnode at given postion

    def insertAtPos(self, newnode, pos):
        if(pos < 0 or pos > self.listLength()):
            print("{ pos } is Invalid postion")
            return
        if(pos == self.listLength()):
            self.insertAtEnd(newnode)
            return
        if(pos == 0):
            self.insertAtHead(newnode)
            return
        current_node = self.head
        current_pos = 0
        previous_node = None
        while(current_pos != pos):
            previous_node = current_node
            current_node = current_node.next
            current_pos += 1
        previous_node.next = newnode
        newnode.next = current_node

    # ---------------------------Deletion Operation on linkedList-------------------------------------------

    # Method to delete head node from the linkedList

    def deleteAtHead(self):
        current_node = self.head
        self.head = current_node.next
        del current_node

    # Method to delete a node at the end of the linkedList
    def deleteAtEnd(self):
        current_node = self.head
        previous_node = None
        while(current_node.next != None):
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        del current_node

    # Method to delete a node at a given postion

    def deleteAtPos(self, pos):
        if(pos < 0 or pos > self.listLength()):
            print("{ pos } is Invalid postion")
            return
        if(pos == self.listLength()):
            self.deleteAtEnd()
            return
        if(pos == 0):
            self.deleteAtHead()
            return
        current_node = self.head
        previous_node = None
        current_pos = 0
        while(pos != current_pos):
            previous_node = current_node
            current_node = current_node.next
            current_pos += 1
        previous_node.next = current_node.next
        del current_node

    # -------------------Helper function used on linkedList operations----------------------------------------

    # Method to return length of the linked list

    def listLength(self):
        current_node = self.head
        length = 0
        while(current_node != None):
            length += 1
            current_node = current_node.next
        return length

    # Method to print the whole list data

    def printList(self):
        current_node = self.head
        if(current_node == None):
            print("List is empty !")
            return
        while(current_node != None):
            print(current_node.data)
            current_node = current_node.next

    # Method to reverse a given linked list

    def reverseList(self):
        current_node = self.head
        previous_pointer = None
        while(current_node != None):
            next = current_node.next
            current_node.next = previous_pointer
            previous_pointer = current_node
            current_node = next
        self.head = previous_pointer

    # Method to search an element in the following linked list

    def searchElement(self, ele):
        current_node = self.head
        index = 0
        noMatch = True
        while(current_node != None):
            index += 1
            if(current_node.data == ele):
                print(f"The element {ele} is found at {index} node")
                noMatch = False
                return
            current_node = current_node.next
        if(noMatch):
            print(f"The element {ele} is not found in following location")


# ------------------------- Creating instance of the linekd list-----------------------------------------

linked = linkedList()

linked.insertAtHead(node(1))
linked.insertAtEnd(node(2))
linked.insertAtEnd(node(3))
linked.insertAtEnd(node(4))
linked.insertAtEnd(node(5))
linked.insertAtPos(node(0), 0)

linked.printList()

linked.deleteAtHead()

print("after head node deletion")

linked.printList()

linked.deleteAtEnd()

print("after end node deletion")

linked.printList()

pos = linked.listLength()

linked.deleteAtPos(pos)

print(f"after deleting {pos} node")

linked.printList()

linked.searchElement(2)

print("\n")

print("After reversing the linkedList")

linked.reverseList()

linked.printList()


