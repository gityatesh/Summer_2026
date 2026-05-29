class node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        
class bst:
    def __init__(self):
        self.root = None
        
    def insertelement(self, root, val):
        if root is None:
            return node(val)
        
        if val<root.data:
            root.left = self.insertelement(root.left, val)
        else: root.right = self.insertelement(root.right, val)
        
    #root left right
    def preorder(self, root):
        if root==None:
            return 
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
    
    #left root right
    def inorder(self, root):
        if root==None:
            return 
        
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)
        
    #left right root
    def postorder(self, root):
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)
        
        
if __name__ == "__main__":
    tree = bst()
    tree.root = tree.insertelement(tree.root, 10)
    tree.root = tree.insertelement(tree.root, 20)
    tree.root = tree.insertelement(tree.root, 4378)
    tree.root = tree.insertelement(tree.root, 187)
    
    tree.inorder(tree.root)