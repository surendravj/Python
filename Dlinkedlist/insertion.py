# Program implementaion of double linked list operations for insertion


# Create node

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Dlink:
    def __init__(self):
        self.head = None

    def is_newNode(self, newnode):
        self.head = newnode
        self.head.prev = None

    def insertAtEnd(self, newnode):
        current_node = self.head
        if(current_node == None):
            self.is_newNode(newnode)
            return
        while(current_node.next != None):
            current_node = current_node.next
        current_node.next = newnode
        newnode.prev = current_node
        newnode.next = None

    def insertAtHead(self, newnode):
        current_node = self.head
        if(current_node == None):
            self.is_newNode(newnode)
            return
        self.head = newnode
        newnode.next = current_node
        newnode.prev = None

    def insertAtPos(self, newnode, pos):
        if(pos == 0):
            self.insertAtHead(newnode)
            return
        current_node = self.head
        previous_node = None
        current_pos = 0
        while(current_pos != pos):
            previous_node = current_node
            current_node = current_node.next
            current_pos += 1
        previous_node.next = newnode
        newnode.prev = previous_node
        newnode.next = current_node
        current_node.prev = newnode

    def printList(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next


dlink = Dlink()

dlink.insertAtEnd(node(1))
dlink.insertAtEnd(node(2))
dlink.insertAtEnd(node(3))
dlink.insertAtHead(node(0))
dlink.insertAtPos(node(7), 2)
dlink.insertAtPos(node(10), 3)
dlink.printList()
