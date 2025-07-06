import re
import string

# method 01
def validate_password(password: str) -> bool:
    lowercase = re.findall("[a-z]", password)
    uppercase = re.findall("[A-Z]", password)
    numbers = re.findall("[0-9]", password)
    pattern = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    pattern_val = pattern.findall(password)

    if ( len(lowercase)> 0 and len(uppercase) > 0 and len(numbers) >0 and len(pattern_val) > 0):
        print("Valid password")
    else:
        print("Invalid password")



# method 02
def validate_password_without_regex(password : str):
    lowercase_letters = list(string.ascii_lowercase)

    uppercase_letters = list(string.ascii_uppercase)

    digits = list(string.digits)

    special_characters = list("!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~")

    global validL
    global validU
    global validD
    global validS
    validL = False
    validU = False
    validD = False
    validS = False
    
    for  letter in lowercase_letters:
        if(letter in password):
            validL = True
        

    for  letter in uppercase_letters:
        if(letter in password):
            validU = True

    for  number in digits:
        if(number in password):
            validD = True

    for  charater in special_characters:
        if(charater in password):
            validS = True

    if (validL and validU and validD and validS):
        print("valid password") 
    else:
        print("invalid password")

def is_valid_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters"
    global has_lower
    has_lower = False
    # has_upper = False
    # has_digits = False
    # has_special = False
    # special_character = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

    for char in password:
        if char.islower():
            has_lower = True

    return has_lower

# validate_password_without_regex("Hello@123")

print(is_valid_password("HELLOWORLd"))