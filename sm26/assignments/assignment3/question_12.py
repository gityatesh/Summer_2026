expenses = [
("Food",200),
("Travel",500),
("Food",150),
("Shopping",1000),
("Travel",200),
("Food",100)
]

exp = {}
for services, expense in expenses:
    exp[services] = exp.get(services,0)+expense
    
print(exp)