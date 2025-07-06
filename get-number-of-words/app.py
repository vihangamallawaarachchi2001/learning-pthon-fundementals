import string

def get_number_of_strings(ls:list):
    count = 0
    for item in ls:
        if item.isalpha():
            count += 1
    return count

def cond(ls:list):
    count = 0
    for word in ls:
        if word[0] == word[-1]:
            count += 1
    return count

print(cond(["abc", "xyz", "aba", "1221", "hello", "mom"]))
