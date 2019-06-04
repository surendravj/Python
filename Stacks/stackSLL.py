# Implementing the stack data structure using linked list


class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.first = None

        # METHOD TO PUSH THE VALUES IN TO THE SATCK
    def push(self, newnode):
        currentNode = self.first
        if(not currentNode):
            self.first = newnode
        else:
            self.first = newnode
            self.first.next = currentNode
        # Method to pop last element from the array

    def pop(self):
        currentNode = self.first
        if(not currentNode):
            print("Stack Underflow")
        else:
            self.first = currentNode.next

        # Method to display the stack

    def display(self):
        currentNode = self.first
        if(not currentNode):
            print("Stack Empty")
        else:
            while(currentNode):
                print(currentNode.data)
                currentNode = currentNode.next


stack = stack()
stack.push(node(1))
stack.push(node(2))
stack.push(node(3))
stack.push(node(4))

stack.display()

stack.pop()
stack.pop()

stack.display()
