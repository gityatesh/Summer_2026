class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    #insert
    def insertathead(self, value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode
        
    def insertattail(self, value):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode
            return
            
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = newnode
        
    def insertatpos(self, value, pos):
        newnode = Node(value)
    
        if pos == 1:
            newnode.next = self.head
            self.head = newnode 
            return
        
        temp = self.head
        count = 1
        
        
        while count < pos - 1 and temp != None:
            temp = temp.next
            count += 1
            
        
        if temp == None:
            print('pos not valid')
            return
            
        newnode.next = temp.next
        temp.next = newnode
        
    def insertaftervalue(self, value, insert_after_value):
        newnode = Node(value)
        temp = self.head
        while temp.data!= insert_after_value and temp!=None:
            temp = temp.next
            
        if temp == None:
            print('value not in list')
            return
        
        newnode.next = temp.next
        temp.next=newnode
        
    # deletion
    def deleteathead(self):
        
        if self.head == None:
            return
        self.head = self.head.next
        
    def deleteattail(self):
        if self.head == None:
            return 
            
        if self.head.next == None:
            self.head = None
            return
        
        temp = self.head
        
        while temp.next.next != None:
            temp = temp.next
            
        temp.next = None
        
    def deleteatpos(self, pos):
        if self.head == None:
            return
            
        if pos == 1:
            self.head = self.head.next
            return 
        
        temp = self.head
        count = 1
        
        
        while count < pos - 1 and temp != None:
            temp = temp.next
            count += 1
            
        if temp == None or temp.next == None:
            print('pos not valid')
            return
            
        temp.next = temp.next.next
        
    #traversal
    def showlinkedlist(self):
        temp = self.head
        
        while temp.next != None:
            print(f"{temp.data}->", end='')
            temp = temp.next
            if temp.next == None:
                print(f"{temp.data}")
                 


if __name__ == "__main__":
    ll = linkedlist()
    ll.insertattail(10)
    ll.insertattail(20)
    ll.insertattail(30)
    
    ll.insertatpos(15, 2) 
    ll.deleteattail()     
    
    ll.showlinkedlist()   