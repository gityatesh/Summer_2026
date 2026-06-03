#using stack
#to run code:
#D:\Summer 2026\main\sm26>python -m assignments.assignment5.question_03
from datastructures.stack import stack

def deletemostrecentaction(actions,remkey):
    tasks = stack()
    for i in range(len(actions)):
        tasks.push(actions[i])
    for i in range(remkey):
        tasks.pop()
        
    tasks.view()
        
actions = [
"Type Hello",
"Type World",
"Delete Last Word",
"Type Python"
]
prev_action_deleted =1
deletemostrecentaction(actions,prev_action_deleted)