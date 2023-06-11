# TODO: Display a welcome message to the user
print("Welcome to Simple PyCalculator")

# TODO: Ask the user to input the first number
num1 = int(input("Input first number: "))

# TODO: Ask the user to select an operation
operation = input("Select an operation: + - * /: ")

# TODO: Ask the user to input the second number
num2 = int(input("Input second number: "))

# TODO: Use Conditional if-else statement to perform necessary arithmetic operations
if operation == "+":
    print("The result is: " + str(num1 + num2))
elif operation == "-":
    print("The result is: " + str(num1 - num2))
elif operation == "*":
    print("The result is: " + str(num1 * num2))
elif operation == "/":
    print("The result is: " + str(num1 / num2))