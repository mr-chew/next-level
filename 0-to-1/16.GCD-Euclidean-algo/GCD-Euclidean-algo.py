# Iterative
def iterative_gcd(x: int, y: int):
    """while loop will continue until y = 0"""
    while(y):
        x,y = y, x%y
    return x

def recursive_gcd(x: int, y: int):
    """keep call the recursive_gcd function until y = 0"""
    if y == 0:
        return x
    return recursive_gcd(y, x%y)

print(f"iterative function gcd(64,48) -> {iterative_gcd(64, 48)}")
print(f"recursive function gcd(64,48) -> {recursive_gcd(48, 64)}")