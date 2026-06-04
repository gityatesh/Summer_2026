
slots = [(1,3),
(2,6),
(8,10),
(8,12),
(8,14),
(8,15),
(15,18), (15,19), ]

s = sorted(slots)
def check(slotslist):
    newslots = []
    
    for i in range(1,len(slotslist)):  #O(n)
        if slotslist[i-1][1] >slotslist[i][0]: 
            # print(f'slots overlapping {slotslist[i-1]} and {slotslist[i]}')
            newslots.append((slotslist[i-1][0],slotslist[i][1]))
            
        else:
            newslots.append(slotslist[i])
    
    for i in range(1,len(newslots)):
        if newslots[i-1][0] == newslots[i][0]:
            newslots[i-1]=0
        
    newslots = [x for x in newslots if x != 0]         
    print(f'new time slots: {newslots}')
    print(f'No of meeting rooms required: {len(newslots)}')
     
check(s)

#time complexity: O(nlogn)
#space complexity: O(n)

