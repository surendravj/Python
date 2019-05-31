class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def lengthList(self):
        temp = self.head
        length = 0
        while(temp.next != None):
            length += 1
            temp = temp.next
        return length
    # insertions methods on linked list

    def insertHead(self, newnode):
        temp = self.head
        self.head = newnode
        self.head.next = temp

    def insertTail(self, newnode):
        temp = self.head
        if(temp == None):
            self.head = newnode
            return
        while(temp.next != None):
            temp = temp.next
        temp.next = newnode

    def insertAt(self, newnode, pos):
        currenpostion = 0
        previousnode = None
        temp = self.head
        if(pos < 0 or pos > self.lengthList()):
            print("Invalid postion to do operation")
            return
        elif(pos == 0):
            self.insertHead(newnode)
        if(temp == None):
            self.insertHead(newnode)
        while(currenpostion != pos):
            previousnode = temp
            temp = temp.next
            currenpostion += 1
        previousnode.next = newnode
        newnode.next = temp

    def printList(self):
        temp = self.head
        if(temp == None):
            print("List is empty")
            return
        else:
            while(temp != None):
                print(temp.data)
                temp = temp.next
    # deletion operations on linked list

    def delete_tail(self):
        temp = self.head
        previousnode = None
        while(temp.next != None):
            previousnode = temp
            temp = temp.next
        previousnode.next = None
        del temp

    def delete_head(self):
        temp = self.head
        self.head = temp.next
        del temp

    def deleteAt(self, pos):
        if(pos < 0 or pos > self.lengthList()):
            print("Invalid postion to do operation")
            return
        elif(pos == 0):
            self.delete_head()
            return
        elif(pos == self.lengthList()):
            self.delete_tail()
            return
        currentpos = 0
        previousnode = None
        currentnode = self.head
        while(currentpos != pos):
            previousnode = currentnode
            currentnode = currentnode.next
            currentpos += 1
        previousnode.next = currentnode.next


linked = linkedList()
linked.insertTail(node(1))
linked.insertTail(node(2))
linked.insertTail(node(3))
linked.insertTail(node(4))
linked.insertHead(node(0))
linked.deleteAt(linked.lengthList()-1)
# linked.insertAt(node(2.5), 2)
linked.printList()
