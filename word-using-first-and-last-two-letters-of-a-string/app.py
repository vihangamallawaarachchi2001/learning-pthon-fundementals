def word_generator(s):
    word = ""

    if len(s) < 2:
        pass
    elif len(str.split(s)) > 1:
        word_arr = str.split(s)
        if len(word_arr[0]) >1 and len(word_arr[0]) <4:
            word=word_arr[0][0] + word_arr[0][1]
        else:
            sen = word_arr[0]
            word = sen[0] + sen[1] + sen[len(sen) -2] + sen[len(sen) -1]
    else:
        word = s[0] + s[1] + s[len(s) -2] + s[len(s) -1]
    return word

def first_and_last_two(s):
    if(len(s) < 2):
        return "It must have at least 2 characters"
    return s[:2] + s[-2:]

print(first_and_last_two("h"))