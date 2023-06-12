# TODO: Display the welcome message for the user
print("Welcome to Python Love Calculator")

# TODO: Prompt the user to enter their name and store it in name1 variable
name1 = input("Enter your name: ")

# TODO: Prompt the user to enter their lover's name and store it in name2 variable
name2 = input("Enter your lover's name: ")

# TODO: Combine the names together
combined_names = name1 + name2

# TODO: Convert the combined names to lowercase
lower_case_str = combined_names.lower()

# TODO: Count the occurrences of "t" in the combined names
t = lower_case_str.count("t")

# TODO: Count the occurrences of "r" in the combined names
r = lower_case_str.count("r")

# TODO: Count the occurrences of "u" in the combined names
u = lower_case_str.count("u")

# TODO: Count the occurrences of "e" in the combined names
e = lower_case_str.count("e")

# TODO: Calculate the sum of "t", "r", "u", and "e" counts
true = t + r + u + e

# TODO: Count the occurrences of "l" in the combined names
l = lower_case_str.count("l")

# TODO: Count the occurrences of "o" in the combined names
o = lower_case_str.count("o")

# TODO: Count the occurrences of "v" in the combined names
v = lower_case_str.count("v")

# TODO: Count the occurrences of "e" in the combined names
e = lower_case_str.count("e")

# TODO: Calculate the sum of "l", "o", "v", and "e" counts
love = l + o + v + e

# TODO: Combine the true and love counts as strings
love_score = str(true) + str(love)

# TODO: Convert the combined love score to an integer
love_score_int = int(love_score)

# Check the love score and print the corresponding message
if love_score_int < 10 or love_score_int > 90:
    print(f"Your love score is {love_score}, you go together like coke and mentos. 💥")
elif love_score_int >= 40 and love_score_int <= 50:
    print(f"Your love score is {love_score}, you are alright together. 😄")
else:
    print(f"Your love score is {love_score} ❤️")