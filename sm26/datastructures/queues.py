class queue:
    def __init__(self, maxvalue=10):
        self.maxvalue = maxvalue
        self.ourqueue = [None] * maxvalue
        
        self.front = -1
        self.rear = -1
        
    def isempty(self):
        return self.rear == -1
    def isfull(self):
        return self.front == self.maxvalue-1
    
    def enqueue(self, value):
        if self.isempty():
            self.front = 0
        if self.isfull():
            return 'queue overflow'
        
        self.rear +=1
        self.ourqueue[self.rear] = value
        
    def dequeue(self):
        if self.isempty():
            return 'queue underflow'
        if self.isfull():
            self.front=self.rear=-1
            
        else:
            print(self.ourqueue[self.front]) 
            self.front +=1
        
        
    def showqueue(self):
        if self.isempty():
            print("Queue is empty.")
            return
            
        for i in range(self.front, self.rear + 1):
            print(self.ourqueue[i])
                
         
         
if __name__ == "__main__":
    q = queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.showqueue()