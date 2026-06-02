def checkavailibility(*regions):
    #now using args we can take multiple regions without changing code
    freq = {}
    for region in regions:
        for id in region: 
            freq[id] = freq.get(id, 0) + 1
    r = []
    for key, val in freq.items():
        if val == 1:
            r.append(key)
    return f'constumer ids in only one region: {sorted(r)}'


region_a = [1, 2, 3, 4, 5,5,5,67]
region_b = [4, 5, 6, 7, 8]
rc = [1,2,3,4,5,6,7,8,9,10]
print(checkavailibility(region_a, region_b,rc))

# print(set(region_a) -set(region_b), set(region_b)-set(region_a))