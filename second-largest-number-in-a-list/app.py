def find_second_largest_number(ls: list):
    largest =ls[0]
    second_largest=ls[0]

    for number in ls:
        if number > second_largest and number > largest:
            second_largest = largest
            largest = number
        if number < largest and number > second_largest:
            second_largest = number
    
    return second_largest
    
print(find_second_largest_number([1,4,-3]))