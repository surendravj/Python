# Implementing the  insertion operation on binary search tree


class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newnode = node(value)
        if(not self.root):
            self.root = newnode
            return self
        else:
            current = self.root
            while(True):
                if(value < current.data):
                    if(not current.left):
                        current.left = newnode
                        return current
                    # insert(current.left,value) recursively
                    current=current.left
                else:
                    if(not current.right):
                        current.right = newnode
                        return current
                    current = current.right
                    # insert(current.right,value) recursively

    def find(self, value):
        Found = False
        current = self.root
        if(not current):
            return None
        while(current and not Found):
            if(current.data > value):
                current = current.left
                # insert(current.left,value) recursively
            elif(current.data < value):
                current = current.right
                # insert(current.right,value) recursively
            else:
                Found = True
                return Found
        return Found


tree = BinarySearchTree()

tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(1)
tree.insert(6)
tree.insert(13)
tree.insert(16)
tree.find(13)
