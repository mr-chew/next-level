def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

operation = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

def perform(a, op, b):
    func=operation[op]
    return func(int(a), int(b))

print("basic calculator - accept two numbers for basic operation")
a = input("first number pls ")
op = input("choose one operation (add, subtract, multiply or divide) ")
b = input("Key in 2nd number ")

print(perform(a, op, b))