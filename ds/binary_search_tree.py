class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value == data:
            return False # duplicates not allowed in tree
        elif self.value > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False
    
    def preorder(self):
        if self:
            print(str(self.value))
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
    
    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.value))
    
    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.value))
            if self.right:
                self.right.inorder()

class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else: 
            self.root = Node(data)
            return True
    
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else: 
            return False
    
    def preorder(self):
        print("PreOrder")
        self.root.preorder()
    
    def postorder(self):
        print("PostOrder")
        self.root.postorder()

    def inorder(self):
        print("InOrder")
        self.root.inorder()
