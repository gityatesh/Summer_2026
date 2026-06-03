expression = "()"
def check(exp):
    checking=''
    count1=1
    
    for i in range(1, len(exp)):
        if exp[i-1]==exp[i]:
            count1+=1
        else:
            checking+=exp[i-1]+str(count1)
            count1=1
    checking+=exp[i]+str(count1)  
    print(checking)
    # if checking[1]== checking[3]:
    #     print('valid')
    # else: print('invalid')  
    flag=0   
    for i in range(1, len(checking)-2,2):
        if checking[i]==checking[i+2]:
            flag+=1
        else: 
            flag=0 
            break
        
    if flag==0:
        return print('invalid')
    else: return print('valid')

check(expression)  