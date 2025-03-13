# Simple Calculator Program

def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    # Perform the operation based on the operator
    if operator == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operator == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operator == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operator == '/':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero")
    else:
        print("Error: Invalid operator")

# Call the calculator function
calculator()