orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza"
]

count={}
for item in orders:
    count[item] = count.get(item, 0) +1
    
print(count)
print(max(count, key = count.get))


