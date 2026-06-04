quantities = [8,4,15,7,12,12]
freq={}
for char in quantities:
    freq[char] = freq.get(char, 0)+1
    
for item,quantity in freq.items():
    if quantity>1:
        print(f'True, {item} appears multiple times')
        break
    else: print('False')
#time complexity: O(n)
#space complexity: O(n)
    
    
#different approach
def check(quantities):
    seen = set()

    for char in quantities:
        if char in seen:
            return print(True)
        seen.add(char)

    return print(False)
check(quantities)

#time complexity: O(n)
#space complexity: O(n)