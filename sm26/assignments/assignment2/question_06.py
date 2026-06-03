#rotate list by k positions
def rotatebykpos(list1,pos:int):
    for i in range(pos+1):
        list1.append(list1[0])
        list1.pop(0)
    
    return list1

#loop for pos+1 no of times
#we'll remove elements from the start of the array as it doesnot effect the i's pos
#but before removing we'll keep appending the list with the 1st element of the list
#this will repeat until the position arrives

numbers = [1, 2, 3, 4, 5]
print(rotatebykpos(numbers,2))
        