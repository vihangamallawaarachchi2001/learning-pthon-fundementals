my_lists = [5,3,8,6,7,2]
list_two = [1,5,3,8,6,7,2,11]
my_list = [1,2,3,4,5,6]

def bubble_sort(lists: list):
    temp = lists.copy()
    u = len(lists) -1
    recursive_loops=0
    count = 0
    while recursive_loops < u +1:
        while(count < u +1 ) :
            if( count != u):
                if( temp[count] > temp[count +1]):
                    temp[count], temp[count +1] = temp[count +1], temp[count]
            count +=1
        recursive_loops +=1
        count = 0
        

    
    return temp

def updated_bubble_sort(lists: list):
    temp = lists.copy()
    n = len(temp)

    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            print(i,j)
            if temp[j] > temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]
                swapped = True
        if not swapped:
            break

    return temp

print(updated_bubble_sort(my_list))