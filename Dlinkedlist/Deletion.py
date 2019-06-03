# inertion and deletion operations on double linked list


# creating node

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# creating linked list

class Dlink:
    def __init__(self):
        self.head = None

    # insertion operations on double linekd list

    def printList(self):
        current_node = self.head
        if(not current_node):
            print("List is empty")
            return
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

    def list_length(self):
        length = 0
        current_node = self.head
        while(current_node):
            length += 1
            current_node = current_node.next
        return length

    def insertAtHead(self, newnode):
        current_node = self.head
        if(not current_node):
            self.head = newnode
            self.head.prev = None
            return
        self.head = newnode
        self.head.next = current_node
        self.head.prev = None

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

    def insertAtPos(self, newnode, pos):
        if(pos < 0 or pos > self.list_length()):
            print(f"{pos} is invalid postion ")
            return
        if(pos == 0):
            self.insertAtHead(newnode)
            return
        if(pos == self.list_length()):
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
        newnode.prev = previous_node
        newnode.next = current_node
        current_node.prev = newnode

    # Deletion opertaions on double linked list

    def deleteAthead(self):
        current_node = self.head
        self.head = current_node.next
        self.head.prev = None

    def deleteAtEnd(self):
        current_node = self.head
        previous_node = None
        while(current_node.next):
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        current_node.prev = None

    def deleteAtpos(self, pos):
        current_node = self.head
        current_pos = 0
        previous_node = None
        if(pos < 0 or pos > self.list_length()):
            print(f"{pos} is invalid postion")
            return
        if(pos == 0):
            self.deleteAthead()
            return
        if(pos == self.list_length()):
            self.deleteAtEnd()
            return
        while(current_pos != pos):
            previous_node = current_node
            current_node = current_node.next
            current_pos += 1
        previous_node.next = current_node.next
        current_node.prev = previous_node

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

    # delete according to the value given

    def deleteByValue(self, ele):
        current_node = self.head
        node_index = -1
        nomatch = True
        while(current_node):
            node_index += 1
            if(current_node.data == ele):
                self.deleteAtpos(node_index)
                nomatch = False
                return
            current_node = current_node.next
        if(nomatch):
            print(f"{ele} is not found to delete")


dlink = Dlink()
dlink.insertAtHead(node(0))
dlink.insertAtHead(node(-1))
dlink.insertAtEnd(node(5))
dlink.insertAtEnd(node(4))
dlink.insertAtEnd(node(3))
dlink.insertAtPos(node(2), 2)
dlink.deleteAthead()
dlink.deleteAtEnd()
dlink.deleteAtpos(3)
dlink.reverseList()
dlink.deleteByValue(10)
dlink.printList()
