def max_val_kay(data: dict):
    return max(data, key=data.get)

print(max_val_kay({'apple': 10, 'banana': 20, 'cherry': 30}))