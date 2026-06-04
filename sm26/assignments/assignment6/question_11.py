#revenue system
revenues = [10,4,3,50,23,90,99]
max = float('-inf')
max2 = float('-inf')
for char in revenues:
    if char>max:
        max= char
for char in revenues:
    if char > max2 and char <max:
        max2 = char        
print(max)
print(max2)

# time complexity: O(n)
# space complexity: O(1)