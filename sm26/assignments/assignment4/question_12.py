    # *********         
    #***********
    # ********* 
    #  *******  
    #   *****
    #    ***
    #     *
   
def makeadiamond(rows):
    k=rows*2+1 
    sp=0
    print(' ', end='')
    for a in range(k-2):
        print('*', end='')
    print()
    for i in range(rows+1):
        for x in range(sp):
            print(' ', end='')
        for j in range(k):
            print('*',end='')
        
        print()
        k-=2
        sp+=1    
        
makeadiamond(7)   