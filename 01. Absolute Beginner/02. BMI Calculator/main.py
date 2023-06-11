# TODO: Display a welcome message to the user
print("Welcome to BMI Calculator")

# TODO: Get user input for weight in kilograms
user_weight = float(input("Enter your weight in kilograms: "))

# TODO: Get user input for height in meters
user_height = float(input("Enter your height in meters: "))

# TODO: Calculate the BMI by dividing weight by the square of height
BMI = user_weight/user_height**2

# TODO: Display the calculated BMI to the user
print("Your BMI is: " + str(BMI))