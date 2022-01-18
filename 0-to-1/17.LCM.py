# Compute LCM Using GCD
# formula -> LCM(a, b) = (a x b) / GCD(a, b)

# reuse code from 16.GCD-Euclidean-algo
def recursive_gcd(x: int, y: int):
    """keep call the recursive_gcd function until y = 0"""
    if y == 0:
        return x
    return recursive_gcd(y, x%y)

def lcm_with_gcd(x: int, y: int):
    return int(x*y / recursive_gcd(x, y))

def iterative_lcm(x: int, y: int):
    """determine which is the smaller number among the 2 integer and do a iterative call of lcm % large_number"""
    if x < y:
        small = x
        large = y
    else:
        small = y
        large = x
    lcm = small
    while lcm%large !=0:
        lcm = lcm + small
    return lcm

print(f"recursive function lcm_with_gcd(99,21) -> {lcm_with_gcd(99, 21)}")
print(f"iterative function iterative_lcm(99,21) -> {iterative_lcm(99, 21)}")