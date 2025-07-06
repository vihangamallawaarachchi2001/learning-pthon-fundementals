my_set = [ 1,2,3, 'hello',4,5, (6,7), 8,9 ]


count = 0
for item in my_set:
    if type(item) == tuple:
        break
    count += 1

print(count)