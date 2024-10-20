def simple_calculator():
    print("welcome to the simple calculator")
    num1 = float(input("Enter the 1st number:"))
    num2 = float(input("Enter the 2nd number:"))
    operation = input("Enter an operation(+,-,*,/):")
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation!"
    return f"The result of {num1} {operation} {num2} is {result}"
print(simple_calculator())
