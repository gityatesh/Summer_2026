#using stack
#D:\Summer 2026\main\sm26>python -m assignments.assignment5.question_06
from datastructures.stack import stack
def reverse(path):
    p=stack()
    for i in range(len(path)):
        p.push(path[i])
        
    print('reversed path')
    p.view()
 
locations = [
"Warehouse",
"Hub-1",
"Hub-2",
"Customer"]   
reverse(locations)
