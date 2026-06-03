#using stack
#to run this code:
#go to terminal D:\Summer 2026\main\sm26> python -m assignments.assignment5.question_01
from datastructures.stack import stack

pages = [
"google.com",
"github.com",
"youtube.com",
"leetcode.com"
]
back_operations =2

def checkhistory(pages, back_operations):
    history = stack()
    for i in range(len(pages)):
        history.push(pages[i])     
    for i in range(back_operations):
        history.pop()
    history.peek()
            
checkhistory(pages,back_operations)    
