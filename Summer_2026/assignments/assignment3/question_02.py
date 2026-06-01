attendance = [
"Aman",
"Rahul",
"Neha",
"Aman",
"Rahul",
"Rahul"
]

attendancelist = {}
for student in attendance:
    attendancelist[student] = attendancelist.get(student,0) + 1
    
print(f'attendance of studnets : {attendancelist}')
print(f'no of unique students: {len(attendancelist)}')