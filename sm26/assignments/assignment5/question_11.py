def checkprevdays(list):
    output =[1]
    for i in range(1, len(list)):
        flag=0
        for j in range(i+1):
            if list[i]==list[j] or list[i]>list[j]:
                flag+=1
        output.append(flag)
        
    return print(output)

prices = [100, 80, 60, 70, 60, 75, 85]
checkprevdays(prices)