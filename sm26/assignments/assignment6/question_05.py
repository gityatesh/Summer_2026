products = [10,20,30,40,50]
new_product = 10

# as list is sorted we can use binary search to add
def findposusingbinary(products, new):
    start = 0
    end = len(products)-1
    
    while start<=end:
        half = start + (end - start)//2
        
        if new < products[half]:
            end = half-1
            
        else: start = half+1
        
    products.insert(start, new)
    print(f'new pos: {start+1}')
    print(products)

findposusingbinary(products, new_product)
#time complexity: O(logn) -> because list is sorted
#space complexity: O(1)


def findpos(products, new):
    for i in range(len(products)):
        
        if new==products[i]:
            print('Product already exists')
            print(f'position: {i+1}')
            break
              
        elif products[i] > new:
            products.insert(i, new)
            print(f'position: {i+1}')
            break
                     
        elif new>products[len(products)-1]:
            print(f'position: {len(products)+1}')
            products.append(new)
            break
  
        else: continue
    
    return print(products)
           
findpos(products, new_product)

# time complexity: O(n)
# splace complexity: O(1)


