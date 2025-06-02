def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operation = input("Choose the operation (+, -, *, /): ")

if operation == "+":
    result = add_numbers(num1, num2)
elif operation == "-":
    result = subtract_numbers(num1, num2)
elif operation == "*":
    result = multiply_numbers(num1, num2)
elif operation == "/":
    result = divide_numbers(num1, num2)
else:
    result = "Invalid operation"
print("The result is:", result)