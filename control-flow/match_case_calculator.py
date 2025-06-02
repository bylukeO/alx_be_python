def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = add_numbers(num1, num2)
    case "-":
        result = subtract_numbers(num1, num2)
    case "*":
        result = multiply_numbers(num1, num2)
    case "/":
        result = divide_numbers(num1, num2)
    case _:
        result = "Invalid operation"

print("The result is:", result)
