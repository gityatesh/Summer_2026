def calcrevenue(rev, key1, key2):
    if key1 < 0 or key2 >= len(rev) or key1 > key2:
        raise IndexError("Invalid keys")
    total = 0
    for i in range(key1, key2 + 1):
        total += rev[i]
    return total
revenues = [100, 200, 150, 300, 250]
key1, key2 = 1, 3
print(calcrevenue(revenues, key1, key2))
# time complexity: O(n)
# space complexity: O(1)
# we can precompute the prefix totals as it saves our time complexity

class calculaterevenue:
    def __init__(self,rev):
        self.prepairedrevlist = []
        summ=0
        for i in range(len(rev)):
            summ += rev[i]
            self.prepairedrevlist.append(summ)
            
    def getrev(self, start, end):
        if start>len(self.prepairedrevlist) or end>len(self.prepairedrevlist) or start < 0:
            return IndexError
        if start==0:
            return self.prepairedrevlist[end]
        return self.prepairedrevlist[end] - self.prepairedrevlist[start-1]
    
query = calculaterevenue(revenues).getrev(1,3)
print(query)

#in this method we generate a list with all prev sums only onetime: O(n)
#now no of queries doesnt matter. It will simply go to index and subtract to give answer. No  need to loop througgh again and again