slots = [
(1,4),
(3,5),
(7,9), 
(8,13)
]
def check(slotslist):
    for i in range(1,len(slotslist)):  #O(n)
        if slotslist[i-1][1] > slotslist[i][0]: 
            print(f'slots overlapping {slotslist[i-1]} and {slotslist[i]}')
        else:
            continue
     
check(slots)
# time complexity: O(n)
# space complexity: O(1)