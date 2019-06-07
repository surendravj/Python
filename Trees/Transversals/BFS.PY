# implementaion of breadth first search in binary search tree


class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if(not self.root):
            self.root = node(val)
            return
        else:
            current_root = self.root
            if(current_root.data == val):
                return None
            while(True):
                if(val < current_root.data):
                    if(not current_root.left):
                        current_root.left = node(val)
                        return
                    current_root = current_root.left
                else:
                    if(not current_root.right):
                        current_root.right = node(val)
                        return
                    current_root = current_root.right

    def BFS(self):
        data = []
        que = []
        currentNode = self.root
        que.append(currentNode)
        while len(que):
            currentNode = que.pop(0)
            data.append(currentNode.data)
            if(currentNode.left):
                que.append(currentNode.left)
            if(currentNode.right):
                que.append(currentNode.right)
        return data

    def findVal(self, value):
        Nomatch = False
        current = self.root
        while(current and not Nomatch):
            if(value < current.data):
                current = current.left
            elif(value > current.data):
                current = current.right
            else:
                Nomatch = True

        return Nomatch


tree = BinarySearchTree()

tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(1)
tree.insert(6)
tree.insert(13)
tree.insert(16)
tree.insert(0)

print(tree.BFS())

print(tree.findVal(55))
