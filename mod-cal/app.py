def mod_calculator(sentence):
    mods = {}
    for char in sentence:
        character_count = 0
        for character in sentence:
            if char == character:
                character_count += 1
        mods.update({char: character_count})
    return mods

print(mod_calculator("hello_world"))

# method 2
def char_freaquency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print(char_freaquency("hello_world"))