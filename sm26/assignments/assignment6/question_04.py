marks = [78,92,65,88,95,70,99,84]
m = sorted(marks, reverse=True)
print(m[:3])
#time complexity: O(nlogn)
#space complexity: O(1)


# can also use min-heap


#other approach
def gettop3(studentlist):
    one=two=three = float('-inf')
    for char in studentlist:
        if char > one:
            three = two
            two = one
            one = char
            
        elif char > two:
            three = two
            two  = char
            
        elif char>three:
            three = char
    return print(f'1st: {one}\n2nd: {two}\n3rd: {three}')
gettop3(marks)    
#time complexity: O(n) as only one loop is running
#space complexity: O(1)


