#greatest sum in a window
def findmaxpatients(patientlist, window):
    seen = []
    for i in  range (len(patientlist)):
        su = sum(patientlist[i:i+window])
        seen.append(su)
        #we'll keep sliding the range until we get all the values
        
    return print(f'{max(seen)}')

visitors = [2,1,5,1,3,2, 10, 5]
window_size = 3
findmaxpatients(visitors, window_size)
#timecomplexity: O(n)
# Space complexity: O(n)



#or we can remove seen
def findmaxpatients2(patientlist, window):
    maxsum=0
    for i in  range (len(patientlist)):
        
        su = sum(patientlist[i:i+window])
        if su>maxsum:
            maxsum = su
        #we'll keep sliding the range until we get all the values  
    return print(f'{maxsum}')

visitors = [2,1,5,1,3,2, 10, 5]
window_size = 3
findmaxpatients2(visitors, window_size)
#timecomplexity: O(n)
# Space complexity: O(1), as we didnt create seen