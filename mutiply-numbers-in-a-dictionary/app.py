num_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
output = 1
for key in num_dict:
    output = output * num_dict.get(key)

print(output)

output = 1
for values in num_dict.values():
    output *= values

print(output)