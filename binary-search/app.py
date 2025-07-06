lists = [4,7,8,12,45,99]

def binary_search(ls:list , search):
    mid_position = int((0 + len(ls) -1) /2)
    mid_value = ls[mid_position]
    lower_bound = ls[0]
    upper_bound = ls[len(ls) -1]
    output = ls[0]

    while output != search:
        if(mid_value < search):
            globals()['lower_bound'] = mid_value
            mid_position = int((mid_position + (len(ls) -1)) /2)
            mid_value = ls[mid_position]
        elif(mid_value < search):
            globals()['upper_bound'] = mid_value
            mid_position = int(0 + mid_position)
            mid_value = ls[mid_position]
        else:
            output = search

    return True
global pos
pos =-1
def search(ls:list, n):
    
    l=0
    u=len(ls) -1

    while l <= u:
        mid = int((l+u) /2)

        if( ls[mid] == n):
            pos = mid
            return True
        else:
            if ls[mid] < n:
                l = mid +1
            else:
                u = mid -1

print(search(lists, 65))