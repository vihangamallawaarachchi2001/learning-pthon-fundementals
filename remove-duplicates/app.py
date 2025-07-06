def duplicate_remover(ls:list):
    freq = {}
    output = []
    for item in ls:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    
    for item in freq:
        if freq.get(item) > 1 :
            output.append(item)
    
    return output, set(ls)

print(duplicate_remover([1,2,3,4,2,5,1,6,3,7]))