# 2*0+1=1
# 2*1+1=3
# 2*2+1=5
# 2*3+1=7

1
121
12321
1234321
rows=5
k=0
for i in range(rows):
    for j in range(i+1):
        k+=1
        print(k, end='')  
    for x in range(i+1, 2*i+1):
        k-=1
        print(k, end='')
    print()
    k-=1
        
        