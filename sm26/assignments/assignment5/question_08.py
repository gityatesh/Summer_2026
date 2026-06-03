#using linkedlist
from datastructures.linkedlist import Node,linkedlist
coaches = [
101,
102,
103,
104
]
new_coach = 105
attach_after = 102
def insertinlist(list, valtobeinserted, insert_after):
    ll = linkedlist()
    print('before')
    
    for i in range(len(list)-1,-1,-1):
        ll.insertathead(list[i])
    ll.showlinkedlist()   
    ll.insertaftervalue(valtobeinserted, insert_after)
    
    print('after')
    ll.showlinkedlist()

insertinlist(coaches, new_coach, attach_after)