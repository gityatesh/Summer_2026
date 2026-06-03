numbers = [5, 8, 3, 1, 9, 6, 2, 7,5]
target = 10

pair = set()

for char in numbers:
    diff = target  - char
    ab = [char, diff]
    absort = sorted(ab)
    pair.add(tuple(absort)) #sets can only store a tuble
        
    
        
        
print(pair)
print(len(pair))

