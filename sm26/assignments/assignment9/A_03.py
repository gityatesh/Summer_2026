branch_b = [1,4,7,10]
branch_a = [2,5,8,12]

for j in range(len(branch_b)):
    for i in range(len(branch_a)):
        if branch_b[j] < branch_a[i]:
            branch_a.insert(i, branch_b[j])
            break
print(branch_a)
# #time complexity: O(n^2)
# #space complexity: O(1)
# #sorting again will add O(nlogn) of time complexity, not good for optimization

        
branch2 = set()
for i in branch_a:
    branch2.add(i)
for j in branch_b:
    branch2.add(j)
print(branch2)
# #time complexity: o(n)
# #space complexity: o(n)

a,b = 0,0
while a<len(branch_a) and b<len(branch_b):
    if branch_b[b]<branch_a[a]:
        branch_a.insert(a, branch_b[b])
        a+=1
        b+=1
    else:
        a+=1        
print(branch_a)
#time complexity: O(n^2) due to insert
#space complexity: O(1)


def merge_sorted_branches(branch_a, branch_b):
    merged = []
    i = 0  # Pointer for branch_a
    j = 0  # Pointer for branch_b

    # Traverse both lists simultaneously
    while i < len(branch_a) and j < len(branch_b):
        if branch_a[i] < branch_b[j]:
            merged.append(branch_a[i])
            i += 1  # Move pointer A
        else:
            merged.append(branch_b[j])
            j += 1  # Move pointer B

    while j < len(branch_b):
        merged.append(branch_b[j])
        j += 1
    while i < len(branch_a):
        merged.append(branch_a[i])
        i += 1
    return merged
print(merge_sorted_branches(branch_a, branch_b))
#time complexity o(n)
#space complexity: o(n)