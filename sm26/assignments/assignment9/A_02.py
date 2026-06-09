customer_ids = [101,101,102,102,103,104,104,105]
def checkduplicates(ids):
    seen = set()
    for i in ids:
        seen.add(i)        
    return seen
print(checkduplicates(customer_ids))
#sorted data doesnot help in this case as hash set automatically sorts and remove duplicates
#complexity: o(n)
#space complexity: o(n)

def checkduplicates2(ids):
    count = 1
    for i in range(1,len(ids)):
        if ids[i]!=ids[i-1]:
            ids[count] = ids[i]
            count+=1
    return ids[:count]
print(checkduplicates2(customer_ids))
#as the list is sorted already so we keep updating numbers in place of count
#tihs way we can find the duplicates without creating a new list

#time complexity: O(n)
#space complexity: o(1) -> improved