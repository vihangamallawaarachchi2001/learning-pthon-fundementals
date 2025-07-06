def remove_target(ls:list, target:any):
    output = ls.copy()
    print(output)
    for item in ls:
        if item == target:
            output.remove(item)
    return output

def remove_occurence(ls:list, target):
    return [item for item in ls if item != target]
print(remove_occurence([1,2,3,1,1], 1))