class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.left = None
        self.right = None
    
    def insert(self, data):
        if data == self.value:
            return False # not allowing duplicates
        elif data < self.value:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                # I forgot return True
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                # forgot to return
                return True
    
    def find(self, data):
        if data == self.value:
            return True
        elif data < self.value:
            if self.left:
                # I forgot to return
                # self.left.find(data)
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                # I forgot to return
                # self.right.find(data)
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
        if not self.root:
            # Forgot to return
            self.root = Node(data)
            return True
        else:
            return self.root.insert(data)
    
    def find(self, data):
        if not self.root:
            return False
        else:
            return self.root.find(data)
    
    def preorder(self):
        print("PreOrder")
        self.root.preorder()
    
    def postorder(self):
        print("PostOrder")
        self.root.postorder()
    
    def inorder(self):
        print("InOrder")
        self.root.inorder()