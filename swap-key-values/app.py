my_dict = {'db': 'sql', 'backend': 'node', 'frontend': 'angular'}

def intrchange_key_val(d1: dict):
    output:dict = {}

    for key, value in d1.items():
        output[value] = key

    return output

print(intrchange_key_val(my_dict))