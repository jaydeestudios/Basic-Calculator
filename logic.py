import math

def advanced_calc(operation, num):
    if operation == "sqrt":
        return math.sqrt(num)
    elif operation == "square":
        return num ** 2
    return "Unknown Operation"

# Example of how you'd call this in a real app
print(f"Square root of 16 is: {advanced_calc('sqrt', 16)}")