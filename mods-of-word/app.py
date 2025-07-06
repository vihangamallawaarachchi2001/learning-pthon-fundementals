import string

def get_mods_of_words(sentence):
    mods = {}
    words = sentence.lower().split()

    for word in words:
        word = word.strip(".,!?")
        if word in mods:
            mods[word] += 1
        else:
            mods[word] = 1

    return mods

sentence = "Hello world! Hello everyone. This is a world of coding"
print(get_mods_of_words(sentence))