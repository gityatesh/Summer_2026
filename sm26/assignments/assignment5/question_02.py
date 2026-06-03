#using queues
#to run code:
#D:\Summer 2026\main\sm26>python -m assignments.assignment5.question_02 in terminal
from datastructures.queues import queue
def showtaskpriority(tasks):
    priority = queue()
    for i in range(len(tasks)):
        priority.enqueue(tasks[i])
    priority.showqueue()
        
    
requests = [
"Request-1",
"Request-2",
"Request-3",
"Request-4"
]

showtaskpriority(requests)  