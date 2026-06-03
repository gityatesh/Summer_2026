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
        return root
        
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
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)
        
        
        
        
        
        
    #finding max and min    
    def findmin(self, currentroot):
        if currentroot == None:
            return 'tree is empty'
        while currentroot.left != None:
            currentroot = currentroot.left
        return currentroot.data   
     
     
     
    def findmax(self, currentroot):
        if currentroot == None:
            return 'tree is empty'
        elif currentroot.right !=None:
            return  self.findmax(currentroot.right)
        else:
            return currentroot.data
             
        
        
        
        
    #finding a value in a tree
    def findaroot(self, currentroot, key):
        if currentroot is None:
            return f'value {key} not found in tree'

        if currentroot.data == key:
            return f'value {key} found in tree'
        elif currentroot.data < key:
            return self.findaroot(currentroot.right, key)
        else:
            return self.findaroot(currentroot.left, key)
        
        
    #to delete a node with a particular value
    def deletenode(self, currentroot, value):
        if currentroot == None:
            return ' tree is empty '
        
        if currentroot.data<value:
            currentroot.right =  self.deletenode(currentroot.right, value)
        elif currentroot.data>value:
            currentroot.left =  self.deletenode(currentroot.left, value)
        
        #3 cases
        #no node 
        #one node(left or right)
        #both nodes 
        
        #now we know that the current root is the root to delete
        else:
            if currentroot.left == None:
                return currentroot.right
            elif currentroot.right == None:
                return currentroot.left
            
            temp = currentroot.right
            while temp.left != None:
                temp = temp.left
                
            currentroot.data = temp.data
            
            currentroot.right = self.deletenode(currentroot.right, temp.data)    
            
        return currentroot       
             
        
if __name__ == "__main__":
    tree = bst()#this command creates a new tree
    tree.root = tree.insertelement(tree.root, 10)#using the current node of the tree we'll insert another node in the treewith different value
    tree.root = tree.insertelement(tree.root, 20)
    tree.root = tree.insertelement(tree.root, 4378)
    tree.root = tree.insertelement(tree.root, 187)
    
    tree.root = tree.deletenode(tree.root, 20)
    
    tree.inorder(tree.root)
    print(tree.findaroot(tree.root, 20))
    
    