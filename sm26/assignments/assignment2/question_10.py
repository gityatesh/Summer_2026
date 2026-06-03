employeeslist =['e1','e2','e3','e4','e5'] 
with open("employees.txt", "w") as doc:
    for names in employeeslist:
        doc.write(names+'\n')
        
with open("employees.txt", "r") as doc:
    read = doc.readlines()
    
for index, name in enumerate(read, start=1):
    print(f'{index}) {name}')
    