import math

def is_square(num):
    if math.sqrt(num).is_integer():
        return True
    return False

x = int(input("Enter a number to check if it is Square -> "))
print (is_square(x))