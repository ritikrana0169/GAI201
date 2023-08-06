def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

division_result = divide_numbers(num1, num2)
print(division_result)
