# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    print(f"Addition: 2 + 3 = {add(2, 3)}")
    print(f"Subtraction: 5 - 2 = {subtract(5, 2)}")
    print(f"Multiplication: 3 * 4 = {multiply(3, 4)}")
    print(f"Division: 8 / 2 = {divide(8, 2)}")
