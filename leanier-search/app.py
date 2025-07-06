list = [5,8,4,6,9,2]
n=9

pos = -1
def search(list, n):
    i = 0

    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i += 1
    
    return False

if search(list, n):
    print("found", pos +1)
else:
    print("Not Found")