dict1 = { 'a': 100, 'b': 200, 'c': 300 }
dict2 = { 'b': 150, 'c': 50, 'd': 400 }

myset = set(list(dict1.keys()) + list(dict2.keys()))
print(myset)

output = {}

for item in myset:
    val1 = 0
    val2 = 0
    if dict1.get(item):
        val1 = dict1.get(item)
        print(f"item at if 1 {item} : {val1} ")
    if dict2.get(item):
        val2 = dict2.get(item)
        print(f"item at if 2 {item} : {val2} ")
    
    output[item] = val1 + val2

print(output)

# method 2
def merger_dict(d1: dict,d2: dict):
    merged = d1.copy()
    for key, value in d2.items():
        merged[key] = merged.get(key,0) + value
    return merged

print(merger_dict(dict1, dict2))