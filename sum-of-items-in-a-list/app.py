def sum(ls: list):
    output = 0
    for item in ls:
        if type(item) is int:
            output = output + item
    return output

print(sum([1, 2,"vihanga",3]))

# type(item) is int