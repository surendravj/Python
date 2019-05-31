# insertion operations on single linked list

# create node


class node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create linked-list


class linked_list:
    def __init__(self):
        self.head = None
    # method to insert a new node as a head node

    def insert_beg(self, newnode):
        temp = self.head
        self.head = newnode
        self.head.next = temp
    # method to find the length of a linked list

    def length_list(self):
        temp = self.head
        length = 0
        while(temp.next != None):
            length += 1
            temp = temp.next
        return length
    # method to insert new nodes at end of linked list

    def insert_end(self, newnode):
        temp = self.head
        if(temp == None):
            self.head = newnode
        else:
            while(temp.next != None):
                temp = temp.next
            temp.next = newnode
    # method to insert new nodes at desired postion

    def insert_mid(self, newnode, position):
        # head->10->20->none || newNode=none||postion=1
        if(position < 0 or position > self.length_list()):
            print("Invalid postion")
            return
        if(position == 0):
            self.insert_beg(newnode)
            return
        temp = self.head
        currentpostion = 0
        while(currentpostion != position):
            previousnode = temp
            temp = temp.next
            currentpostion += 1
        previousnode.next = newnode
        newnode.next = temp
    # method to print the whole linked list

    def printList(self):
        temp = self.head
        if(temp == None):
            print("list is empty")
        else:
            while(temp != None):
                print(temp.data)
                temp = temp.next


linked = linked_list()

linked.insert_end(node("surendra"))
linked.insert_end(node("mani"))
linked.insert_end(node("harshe"))
# linked.printList()
linked.insert_beg(node("praneeth"))
# linked.printList()
linked.insert_mid(node("king2"), 7)
linked.printList()
