inventory = [
("Laptop",10),
("Mouse",25),
("Laptop",5),
("Keyboard",8),
("Mouse",10)
]
ourlist = {}
for item, count in inventory:
    ourlist[item] = ourlist.get(item, 0) + count
    
print(ourlist)