records = [
("Rahul","09:00"),
("Aman","09:10"),
("Rahul","12:00"),
("Rahul","17:00"),
("Aman","15:00")
]
count={}
for employee,time in records:
    count[employee] = count.get(employee, 0) + 1
    
print(count)
print(max(count, key = count.get))