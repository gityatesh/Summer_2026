visits = [5,3,4,5,3,6,4]
freq = {}
for id in visits:  #O(n)
    freq[id] = freq.get(id, 0) + 1

print(freq)
for id, key in freq.items():  #O(n)
    if key ==1:
        print(f'{id} is a unique customer')
        
# time commplexity: O(n)
# space complexity: O(n)