class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Q:
    def __init__(self):
        self.first = None

    def Enqueue(self, newnode):
        currentNode = self.first
        if(not currentNode):
            self.first = newnode
        else:
            while(currentNode.next):
                currentNode = currentNode.next
            currentNode.next = newnode

    def Dequeue(self):
        currentNode = self.first
        if(not currentNode):
            print("Overflow")
        else:
            self.first = currentNode.next

    def display(self):
        currentNode = self.first
        if(not currentNode):
            print("Q is empty")
        else:
            while(currentNode):
                print(currentNode.data)
                currentNode = currentNode.next


q = Q()

q.Enqueue(node("king"))

q.Enqueue(node("queen"))

q.Enqueue(node("soldier"))

q.Enqueue(node("joker"))

q.display()

print("\n")

q.Dequeue()

q.Dequeue()

q.display()
