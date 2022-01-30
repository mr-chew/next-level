import random
import string

def pass_gen(length, lower=True, upper=True, digit=True, punctuation=True):
    char =""
    if lower:
        char += string.ascii_lowercase
    if upper:
        char += string.ascii_uppercase
    if digit:
        char += string.digits
    if punctuation:
        char += string.punctuation
    
    generate_pass = ''.join(random.choice(char) for i in range((length)))
    return generate_pass

password = pass_gen(26)
print(password)
    
            