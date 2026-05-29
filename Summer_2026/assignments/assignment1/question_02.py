#to find the 2nd largest element
def find2ndlargest(ourarr):
    for i in range(len(ourarr)):
        for j in range (len(ourarr)):
            if ourarr[i]<ourarr[j]:
                ourarr[i], ourarr[j] = ourarr[j], ourarr[i]
                #bubble sort
                
    return ourarr[len(ourarr)-2]

arra1= [4, 8, 2, 10, 6]
print(find2ndlargest(arra1))
    