def get_repeated_numbers(t: tuple):
    output = []
    prev = []
    for item in t:
        if( item in prev):
            output.append(item)
        else:
            prev.append(item)

    return output

my_tuple = (1,2,1,3,4,5,4,6,8,6)
print(get_repeated_numbers(my_tuple))