import math

def prime_factorization(num: int):
    #handle edge case prime_factorization(1)
    if num == 1:
        return [1]
    
    # create empty list -> prime factors
    factors = []
    prime = 2
    
    # compute number of 2 that divide num
    while num % prime == 0:
        factors.append(prime)
        num = num / prime
        
    # will be odd number now and check for odd number only, for loop increment by 2 each time
    # the range will be start from 3 to square root(num)
    for i in range(3, int(math.sqrt(num))+1, 2):
        while num % i == 0:
            factors.append(i)
            num = num / i
            
    # if we have a number (num) that is greater than 2 at the end, this is also a prime
    if num > 2:
        factors.append(int(num))
        
    return factors

x = int(input("Enter a positive integer value -> "))
print (prime_factorization(x))