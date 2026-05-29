#we'll create a class for node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    #linkedlist is empty initially
    def __init__(self):
        self.head = None
    
    #insertion
    def insertathead(self, value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode
        
    def insertattail(self, value):
        newnode=Node(value)
        if self.head == None:
            self.head = newnode
            return
            
        temp=self.head
        while temp.next != None:
            temp = temp.next
        temp.next = newnode
        
    def insertatpos(self, value, pos):
        newnode = Node(value)
        temp = self.head
        
        if pos == 1:
            newnode.next = self.head
            return
        
        count = 1
        if count<pos:
            temp = temp.next
            count+=1
        elif count==pos:
            newnode.next = temp.next #forming the link in bw the previous node and next node
            temp.next = newnode
        else:
            print('pos not valid')
            return
        
    #deletion
    def deleteathead(self):
        if self.head.next == None:
            self.head = None
            return
        self.head = self.head.next
        
    def deleteattail(self):
        if self.head.next == None:
            self.head = None
            return 
        
        temp = self.head
        if temp.next.next != None:
            temp = temp.next
        temp.next = None
        
    def deleteatpos(self, pos):
        if pos==1:
            self.head= self.head.next
            return 
        
        temp = self.head
        count =1
        while pos<count-1:
            temp = temp.next
            
        temp.next = temp.next.next
        
        
    #traversail
    def showlinkedlist(self):
        pass            
            