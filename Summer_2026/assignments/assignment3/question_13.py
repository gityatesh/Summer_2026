paragraph = "Python is easy. Python is powerful. Python is popular."
freq = {}
newpar = paragraph.lower().split(' ') # this will make paragraph in lower cases and also split them on the bases of space
for char in newpar:
    freq[char] = freq.get(char, 0) + 1
    
    
print(freq)
    