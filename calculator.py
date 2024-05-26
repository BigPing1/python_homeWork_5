def add (a, b):
    result = a + b
    return print(f"result: {result}")

def subtract (a, b):
    result = a - b
    return print(f"result: {result}")

def multiply (a, b):
    result = a * b
    return print(f"result: {result}")

def divide (a, b):
    result = a / b
    if a == 0 or b == 0:
        return print("Wrong number zero")
    return print(f"result: {result}")

