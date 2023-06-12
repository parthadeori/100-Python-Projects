# Display a welcome message to the user.
print("Welcome to Python Tip Calculator 🧮")

# Prompt the user to enter the bill amount
bill_amount = float(input("Enter the total bill amount: $"))

# Prompt the user to enter the tip percentage
tip_percentage = float(input("Enter the tip percentage (e.g., 15, 18, 20): "))

# Prompt the user to enter the number of people
num_people = int(input("Enter the number of people to split the bill: "))

# Calculate the tip amount
tip_amount = bill_amount * (tip_percentage / 100)

# Calculate the total amount including tip
total_amount = bill_amount + tip_amount

# Calculate the individual share
individual_share = total_amount / num_people

# Print the summary of the bill
print("----- Tip Calculator Summary -----")
print(f"Total bill amount: ${bill_amount:.2f}")
print(f"Tip percentage: {tip_percentage}%")
print(f"Number of people: {num_people}")
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount (including tip): ${total_amount:.2f}")
print(f"Individual share: ${individual_share:.2f}")
print("----------------------------------")
