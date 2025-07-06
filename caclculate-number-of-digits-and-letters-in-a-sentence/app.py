print("Enter alphanumeric sentnce : ", end="")
sentence = input()
alpha_count = 0
num_count = 0
for i in sentence:
    if (str.isdigit(i)):
        num_count += 1
    elif (str.isalpha(i)):
        alpha_count += 1

print(f"alpha = {alpha_count} \nnumeric = {num_count}")