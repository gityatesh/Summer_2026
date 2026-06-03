#using linkedlist
from datastructures.linkedlist import Node,linkedlist
numbers = [5, 2, 8, 1, 7]
new_number = 6
insert_after = 1
def insertinlist(list, valtobeinserted, insert_after):
    ll = linkedlist()
    print('before')
    
    for i in range(len(list)-1,-1,-1):
        ll.insertathead(list[i])
    ll.showlinkedlist()   
    ll.insertaftervalue(valtobeinserted, insert_after)
    
    print('after')
    ll.showlinkedlist()

insertinlist(numbers, new_number, insert_after)

#made a new func in original linkedlist file for inserting after given value