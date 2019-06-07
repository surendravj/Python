# Implementaion of binary search tree and some transversals


# Creating node
class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


# creating Tree

class BinarySearchTree:
    def __init__(self):
        self.root = None
    # method to insert values at current position

    def insert(self, val):
        newnode = node(val)
        if(not self.root):
            self.root = newnode
            return
        current = self.root
        while(True):
            if(val == current.data):
                return ValueError
            if(val < current.data):
                if(not current.left):
                    current.left = newnode
                current = current.left
            else:
                if(not current.right):
                    current.right = newnode
                    return
                current = current.right
    # Method to transverse the tree horizontally

    def BFS(self):
        data = []
        visited = []
        current = 0
        visited.append(self.root)
        while(len(visited)):
            current = visited.pop(0)
            data.append(current.data)
            if(current.left):
                visited.append(current.left)
            if(current.right):
                visited.append(current.right)
        return data

    def DFS_preOrder(self):
        data = []
        visited = []
        current = 0
        visited.append(self.root)
        while(len(visited)):
            current = visited.pop()
            data.append(current.data)
            if(current.right):
                visited.append(current.right)
            if(current.left):
                visited.append(current.left)
        return data

    def DFS_inOrder(self):
        data = []

        def inorder(node):
            if(node.left):
                inorder(node.left)
            data.append(node.data)
            if(node.right):
                inorder(node.right)                      
        inorder(self.root)
        return data

    def DFS_postOrder(self):
        data = []
        def postorder(node):
            if(node.left):
                postorder(node.left)
            if(node.right):
                postorder(node.right)
            data.append(node.data)
        postorder(self.root)
        return data

tree = BinarySearchTree()

tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(1)
tree.insert(6)
tree.insert(13)
tree.insert(16)
print(tree.BFS())
print(tree.DFS_preOrder())
print(tree.DFS_inOrder())
print(tree.DFS_postOrder())