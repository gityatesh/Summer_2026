visitors = [
"Rahul",
"Aman",
"Rahul",
"Neha",
"Aman",
"Rahul"
]

freq = {}
for visitor in visitors:
    freq[visitor] = freq.get(visitor,0)+1
#using same traversal logic explained today   
print(f'frequencies: {freq}')
print(f'max number of visits by: {max(freq, key = freq.get)}')
    