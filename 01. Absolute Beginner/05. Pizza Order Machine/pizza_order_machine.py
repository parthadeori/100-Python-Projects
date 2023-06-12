# Prompt the user to choose a pizza size
print("Welcome to Pizza World!")
print("Please select a pizza size:")
print("1. Small")
print("2. Medium")
print("3. Large")
size_choice = int(input("Enter your choice (1-3): "))

# Process the user's choice and calculate the price
if size_choice == 1:
    pizza_size = "Small"
    price = 10.99
elif size_choice == 2:
    pizza_size = "Medium"
    price = 12.99
elif size_choice == 3:
    pizza_size = "Large"
    price = 14.99
else:
    print("Invalid choice. Please try again.")
    exit()

# Prompt the user to choose a pizza topping
print("Please select a pizza topping:")
print("1. Pepperoni")
print("2. Mushrooms")
print("3. Extra cheese")
topping_choice = int(input("Enter your choice (1-3): "))

# Process the user's choice and update the price
if topping_choice == 1:
    pizza_topping = "Pepperoni"
    price += 1.99
elif topping_choice == 2:
    pizza_topping = "Mushrooms"
    price += 0.99
elif topping_choice == 3:
    pizza_topping = "Extra cheese"
    price += 1.49
else:
    print("Invalid choice. Please try again.")
    exit()

# Display the order details and total price
print("Your order summary:")
print(f"Pizza size: {pizza_size}")
print(f"Pizza topping: {pizza_topping}")
print(f"Total price: ${price:.2f}")
print("Thank you for your order. Enjoy your pizza!")