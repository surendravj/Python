# Implementaion of binary search tree and it operations


# created nodes

class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


# creating tree using root

class BinarySearchTree:
    def __init__(self):
        self.root = None
    # Method to insert newn nodes in to the tree

    def insert(self, val):
        newnode = node(val)
        if(not self.root):
            self.root = newnode
            return
        current = self.root
        while(True):
            if(val < current.data):
                if(not current.left):
                    current.left = newnode
                    return
                current = current.left
            else:
                if(not current.right):
                    current.right = newnode
                    return
                current = current.right
    # Method to check given value is there or not  in a given tree

    def contains(self, val):
        found = False
        if(not self.root):
            return None
        if(self.root.data == val):
            return True
        else:
            current = self.root
            while(current and not found):
                if(val < current.data):
                    current = current.left
                elif(val > current.data):
                    current = current.right
                else:
                    found = True
            return found

    # Searching techniques  or transeversals methodd to transverse a tree

    # Breadth-First-Search

    def BFS(self):
        data = []
        visted = []
        current = 0
        visted.append(self.root)
        while(len(visted)):
            current = visted.pop(0)
            data.append(current.data)
            if(current.left):
                visted.append(current.left)
            if(current.right):
                visted.append(current.right)
        return data

    # ---------------------- Death-First-search---------------------------

    # pre-order (root,left,right)

    def preOrder(self):
        data = []
        def preOrder(node):
            data.append(node.data)
            if(node.left):
                preOrder(node.left)
            if(node.right):
                preOrder(node.right)
        preOrder(self.root)
        return data

    # in-order (left,root,right)

    def inOrder(self):
        data = []
        def inorder(node):
            if(node.left):
                inorder(node.left)
            data.append(node.data)
            if(node.right):
                inorder(node.right)
        inorder(self.root)
        return data

    #post-order (left,right,root)

    def postOrder(self):
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
print("BFS")
print(tree.BFS())
print("preorder")
print(tree.preOrder())
print("inorder")
print(tree.inOrder())
print("postorder")
print(tree.postOrder())
print(tree.contains(162))
