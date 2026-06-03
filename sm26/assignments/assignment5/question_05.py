#using queue
#D:\Summer 2026\main\sm26>python -m assignments.assignment5.question_05

from datastructures.queues import queue
passengers = [
"A",
"B",
"C",
"D",
"E"
]
available_tickets = 3

def checkpassangers(passengers, tix):
    p = queue()
    for i in range(len(passengers)):
        p.enqueue(passengers[i])
    print('served: ')    
    for i in range(tix):
        p.dequeue()
    
    print('waiting: ')
    p.showqueue()
    
checkpassangers(passengers, available_tickets)