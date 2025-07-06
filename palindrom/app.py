print("Enter a word : ", end="")
word = input()
rversed_word = word[::-1]
if(word == rversed_word):
    print("This is a palandrom")
else:
    print("This is not a palandrom")