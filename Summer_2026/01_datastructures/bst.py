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
        
    #finding max and min    
    def findmin(self, currentroot):
        if currentroot == None:
            return 'tree is empty'
        while currentroot !=None:
            currentroot = currentroot.left
        return currentroot.data   
     
    def findmax(self, currentroot):
        if currentroot == None:
            return 'tree is empty'
        while currentroot !=None:
            currentroot = currentroot.right
        return currentroot.data       
        
        
    #finding a value in a tree
    def findaroot(self, currentroot, key):
        if currentroot == None:
            return 'tree is empty'
        
        if currentroot.data == key:
            return f'value found in tree'
        while currentroot.data<key:
            currentroot = self.findaroot(currentroot.right, key)
        while currentroot.data>key:
            currentroot = self.findaroot(currentroot.left, key)
        else: return 'no such root with value {key} is found'
             
        
        
if __name__ == "__main__":
    tree = bst()#this command creates a new tree
    tree.root = tree.insertelement(tree.root, 10)#using the current node of the tree we'll insert another node in the treewith different value
    tree.root = tree.insertelement(tree.root, 20)
    tree.root = tree.insertelement(tree.root, 4378)
    tree.root = tree.insertelement(tree.root, 187)
    
    tree.inorder(tree.root)