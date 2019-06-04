# implementing Qs using array data structures


class Q:
    def __init__(self):
        self.q = []

    def is_empty(self):
        return len(self.q) == 0

    def Enqueue(self, item):
        self.q.insert(0, item)

    def Dequeue(self):
        if(self.is_empty()):
            print("Q overflow")
            return
        return self.q.pop()

    def display(self):
        if(self.is_empty()):
            print("Q is empty")
            return
        print(self.q)


q = Q()
q.Enqueue("king")
q.Enqueue("king11")
q.Enqueue("king22")
q.display()
q.Dequeue()
# q.Dequeue()
# q.Dequeue()
q.Dequeue()
q.display()
