numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = int(input("Enter a number to generate its multiplication table: "))
for i in numbers:
    result = number * i
    print(f"{number} x {i} = {result}")