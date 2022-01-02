# create a program that generates a random number using the random library
# importing library
import random as rnd

print(f"random floating point {rnd.random()}")

a =1
b =10
s=1
rnd.seed(s)
print(f"using rnd.seed({s})")
print(f"random int from {a} to {b} -> {rnd.randint(a, b)}")
print(f"random int from {a} to {b} -> {rnd.randint(a, b)}")
print(f"random int from {a} to {b} -> {rnd.randint(a, b)}")
print(f"random int from {a} to {b} -> {rnd.randint(a, b)}")
rnd.seed(s)
print(f"random int from {a} to {b} -> {rnd.randint(a, b)}\n")

state=rnd.getstate()
rnd.setstate(state)
print(f"using rnd.setstate()")
print(f"random int from {a} to {b} -> {rnd.randint(a, b)}")
print(f"random int from {a} to {b} -> {rnd.randint(a, b)}")
print(f"random int from {a} to {b} -> {rnd.randint(a, b)}")
rnd.setstate(state)
print(f"random int from {a} to {b} -> {rnd.randint(a, b)}")
print(f"random int from {a} to {b} -> {rnd.randint(a, b)}")
print(f"random int from {a} to {b} -> {rnd.randint(a, b)}\n")

# randint() vs randrange() to equivalent to
# randrange (a, b+1)  vs randrange (a, b)
rnd.seed(s)
print(f"random int from {a} to {b} -> {rnd.randrange(a, b)}")
print(f"random int from {a} to {b} -> {rnd.randrange(a, b)}")
print(f"random int from {a} to {b} -> {rnd.randrange(a, b)}\n")

# random number with 8 bits
rnd.seed(s)
print(f"rnd.getrandbits(8) is -> {rnd.getrandbits(8)}\n")
