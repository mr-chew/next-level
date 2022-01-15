import math

def is_square(num):
    if math.sqrt(num).is_integer():
        return True
    return False

print (is_square(144))
print (is_square(123))