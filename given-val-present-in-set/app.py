my_set = { 1,2,3,4,5 }

def value_remover(s:set,target):
    output = s.copy()
    output.remove(1)
    return output

print(value_remover(my_set, 3))

