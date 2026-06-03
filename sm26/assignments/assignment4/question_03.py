def checkabsentees(attendencelist, r1st,rlast):
    absentees =[]
    for rollno in range(r1st, rlast+1):
        if rollno not in attendencelist:
            absentees.append(rollno)
            
    return f'Absentees: {absentees}'

submitted_rolls = [101, 102, 104, 105, 107, 110]
print(checkabsentees(submitted_rolls, 101,110))
    