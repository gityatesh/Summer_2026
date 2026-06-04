#check employee id
def checkid(id_list, id):
    #as the data is already sorted
    start = 0
    end = len(id_list)-1
    
    while start<=end:
        half = start + (end-start)//2               #O(logn)
        if id_list[half] == id:
            return print(f'yes id found!!: { id}')
        
        elif id_list[half]<id:
            start = half+1
        else:
            end = half-1       
    return print('Id not found')

employee_ids = [101,102,103,104,105,106,107,108,109]
id = 109
checkid(employee_ids, id)

#time complexity: O(logn)
#space complexity: O(1)



#if id_list not sorted 
def checkid2(id_list, id):
    for i in id_list:
        if i == id:
            return print(f'Yes id found: {i}')
    return print('id not found')
employee_ids = [101,102,103,104,105,106,107,108,109]
id = 107
checkid2(employee_ids, id)

#time complexity: O(n)
#space complexity: O(1)