import string
print("Enter the sentence : ", end="")
sentence = input()
output = ""
for i in range( len(sentence)-1, -1, -1):
    output = output + sentence[i]

print(output)
print(sentence[::-1])