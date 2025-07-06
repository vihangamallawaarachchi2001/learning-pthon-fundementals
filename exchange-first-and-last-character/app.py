def swap_first_and_last_letters(s):
    if len(s) < 2:
        return "Not long enough"
    return s[-1] + s[1:-1] + s[0]

print(swap_first_and_last_letters("python"))