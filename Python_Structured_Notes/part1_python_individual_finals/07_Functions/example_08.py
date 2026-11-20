def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
print(add(8, 2))
print(subtract(8, 2))
print(multiply(8, 2))
print(divide(8, 2))
