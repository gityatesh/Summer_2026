revenues = [100,200,150,300,250]

def prevsum(rev):
    final=[]
    sumo = rev[0]
    final.append(sumo)
    for i in range(1,len(rev)):
        final.append(sumo+rev[i])
        sumo = sumo+rev[i]
    return final
print(prevsum(revenues))

#each position reprsent the sums of the previous values
#prev calculations are used so that python dont have to recalculate the whoel list again
#time complexity: O(n)
#space complexity: O(n) due to final that we created
#we have a list of revenues where each element = revenue till then. in reporting if we are asked to tell the revenue till 68th day, we can easily tell that but finding the value on 67th index


def prevsum2(rev):
    for i in range(1,len(rev)):
        rev[i] = rev[i]+rev[i-1]
    return rev
print(prevsum2(revenues))
# time complexity: O(n)
#space complexity: O(1)