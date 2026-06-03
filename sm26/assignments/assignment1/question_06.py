students = ['s1','s2','s3','s4','s5']
#writing
with open('students.txt', 'w') as file1:
    for name in students:
        file1.write(name + '\n')
#reading      
with open('students.txt', 'r') as file1:
    lines = file1.readlines()
#listing the students  
for index,name in enumerate(lines, start=1):
    print(f'{index}) {name}')
    