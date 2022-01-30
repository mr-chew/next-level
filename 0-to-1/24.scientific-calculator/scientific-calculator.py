import math

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def square(a):
    return a**2

def sqrt(a):
    return math.sqrt(a)

def log(a):
    return math.log(a)

def exp(a, b):
    return a**b

operation = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "square": square,
    "square root": sqrt,
    "log": log,
    "exponentiate": exp
}

def perform(a, op, b):
    func=operation[op]
    return func(int(a), int(b))

def perform2(a, op):
    func=operation[op]
    return func(int(a))


print("Scientific calculator")
op = input("choose one operation (add / subtract / multiply / divide / square / square root / log) ")

if op in ["square", "square root", "log"]:
    a = input("Number pls ")
    print(perform2(a, op))
else:
    a = input("first number pls ")
    b = input("Key in 2nd number ")
    print(perform(a, op, b))