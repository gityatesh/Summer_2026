class stack:
    
    def __init__(self, maxlimit = 10):
        self.maxlimit = maxlimit
        self.ourarr = [None]*self.maxlimit #this func will multiply the None inside list i.e. [None, None, None.....]
        self.top = -1
        
    def isempty(self)->bool:
        return self.top == -1
        # if self.top==-1:return True
        # else:return False 
    def isfull(self)->bool:
        return self.top == self.maxlimit-1
        # if self.top == self.maxlimit-1:return True
        # else: return False
        
    def push(self, item):
        if self.isfull():
            print('stack is full')
            return
        else: 
            self.top+=1
            self.ourarr[self.top] = item
            
    def pop(self):
        if self.isempty():
            print('stack already empty')
            return
        else:
            # print(self.ourarr[self.top]) 
            self.top -=1
            
    def peek(self):
        if self.isempty():
            print('stack is empty')
            return
        else: print(self.ourarr[self.top])
    
    def view(self):
        if self.isempty():
            print('stack is empty')
            return
        else:
            for i in range(self.top, -1,-1):
                print(self.ourarr[i])
        
if __name__ == '__main__':
    browser_history = stack()
    browser_history.push('google.com')
    browser_history.push('wikipedia.com')
    browser_history.pop()
    browser_history.view()
    
    
            
        