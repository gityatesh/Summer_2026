#to find duplicate elements from an array
def findduplicate(arr1):
    duplicates = []
    for i in range(len(arr1)):
        for j in range(i+1, len(arr1)):
            if arr1[i]==arr1[j]:
                if arr1[i] not in duplicates:
                    duplicates.append(arr1[i])
    return duplicates

# create new array and add only duplicate elements

numbers = [1, 2, 3, 2, 4, 5, 1, 6,6,6,6,6,6]
print(findduplicate(numbers))
                