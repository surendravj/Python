# Double linekd list implementaion and its operations


# Creating Nodes

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


#  Creating linkedLists

class Dlink:
    def __init__(self):
        self.head = None

    # -------------- insertion operations on double linked lists----------------------

    # Method to insert a newnode at head postion

    def insertAtHead(self, newnode):
        current_node = self.head
        if(not current_node):
            self.head = newnode
            self.head.prev = None
            return
        self.head = newnode
        self.head.next = current_node
        self.head.prev = None

    # Method to insert newnode at end of the postion

    def insertAtEnd(self, newnode):
        current_node = self.head
        if(not current_node):
            self.head = newnode
            self.head.prev = None
            return
        while(current_node.next):
            current_node = current_node.next
        current_node.next = newnode
        newnode.prev = current_node

    # Method to insert newnode at given postion or in between two nodes

    def insertAtPos(self, newnode, pos):
        if(pos < 0 or pos > self.list_Length()):
            print(f"{ pos } is invalid postion")
            return
        if(pos == 0):
            self.insertAtHead(newnode)
            return
        if(pos == self.list_Length()):
            self.insertAtEnd(newnode)
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
        newnode.prev = previous_node
        current_node.prev = newnode

    # -------Helper functions that are used while implementing any linked list type--------

    # Method to print the linked list data

    def printList(self):
        current_node = self.head
        if(not current_node):
            print("List is empty")
            return
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

    # Method to return the total length of the linked list

    def list_Length(self):
        length = 0
        current_node = self.head
        while(current_node):
            length += 1
            current_node = current_node.next
        return length

    # Method used to search an element in following linked list

    def searchElement(self, ele):
        current_node = self.head
        noMatch = True
        node_index = 0
        while(current_node):
            node_index += 1
            if(current_node.data == ele):
                print(f"The element {ele} is found at {node_index} node")
                noMatch = False
                return
            current_node = current_node.next
        if(noMatch):
            print("No match found un the following linked list")

    # Method to reverse given lineked list

    def reverseList(self):
        current_node = self.head
        previous_pointer = None
        while(current_node):
            next_item = current_node.next
            current_node.next = previous_pointer
            current_node.prev = next_item
            previous_pointer = current_node
            current_node = next_item
        self.head = previous_pointer

    # ------------------ Deletion operations on linked list-------------------------------------

    # Method to delete head node

    def deleteAtHead(self):
        current_node = self.head
        self.head = current_node.next
        self.head.prev = None
        del current_node

    # Method to delete end node

    def deleteAtEnd(self):
        current_node = self.head
        previous_node = None
        while(current_node.next):
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        current_node.prev = None
        del current_node

    # Method to delete a node at given position

    def deleteAtPos(self, pos):
        if(pos < 0 or pos > self.list_Length()):
            print(f" {pos} is Invalid postion ")
            return
        if(pos == 0):
            self.deleteAtHead()
            return
        if(pos == self.list_Length()):
            self.deleteAtEnd()
            return
        current_node = self.head
        current_pos = 0
        previous_node = None
        while(current_pos != pos):
            previous_node = current_node
            current_node = current_node.next
            current_pos += 1
        previous_node.next = current_node.next
        current_node.prev = previous_node

    # Method to delete a node by value

    def DeleteByValue(self, value):
        node_index = -1
        current_node = self.head
        noMatch = True
        while(current_node):
            node_index += 1
            if(current_node.data == value):
                self.deleteAtPos(node_index)
                noMatch = False
                return
            current_node=current_node.next
        if(noMatch):
            print("No element is found")


dlink = Dlink()

dlink.insertAtEnd(node(1))
dlink.insertAtEnd(node(2))
dlink.insertAtEnd(node(3))
dlink.insertAtEnd(node(4))
dlink.insertAtHead(node(0))
dlink.insertAtPos(node(2.5), 3)
dlink.insertAtPos(node(4.5), dlink.list_Length())
dlink.printList()

# dlink.reverseList()
# print("AFTER REVERSING THE LINKED LIST")
# dlink.printList()

# # dlink.searchElement(1)


dlink.DeleteByValue(4.5)
dlink.deleteAtPos(3)
dlink.printList()
dlink.reverseList()
print("AFTER REVERSING THE LINKED LIST")
dlink.printList()
