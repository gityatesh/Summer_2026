#using brute force
revenues = [2,4,7,11,15]
target = 17
def checkpairs(rev,key):
    for i in range(len(revenues)):
        for j in range(i):
            if revenues[i]+revenues[j]==target:
                return True
    return False
print(checkpairs(revenues,target))

#using the hash set we can avoid checking every pair
def checkpair2(rev, key):
    seen = set()#hash set: takes extra o(n) space but saves o(n) time
    for i in rev:
        missing = key-i
        if missing in seen:
            return True
        seen.add(i)        
    return False
print(checkpair2(revenues,target))