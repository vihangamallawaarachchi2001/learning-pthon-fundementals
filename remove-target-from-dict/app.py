def remove_target_value_keys(d1: dict, target):
    output = d1.copy()
    for key,value in d1.items():
        if( value == target ):
            output.pop(key)
    
    return output

print(remove_target_value_keys({
    'apple': 50,
    'banana': 0,
    'cherry': 75,
    'date': 0
}, 0))

def method_2(d1: dict, target):
    return { key:value for key, value in d1.items() if value != target }

print(method_2({
    'apple': 50,
    'banana': 0,
    'cherry': 75,
    'date': 0
}, 0))