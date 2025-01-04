# calculator.py
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the quotient of two numbers. Handles division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    print("Addition: 5 + 3 =", add(5, 3))
    print("Subtraction: 5 - 3 =", subtract(5, 3))
    print("Multiplication: 5 * 3 =", multiply(5, 3))
    print("Division: 5 / 3 =", divide(5, 3))
