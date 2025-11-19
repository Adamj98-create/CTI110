# Adam Jones

# 19 NOV 2025

# P3LAB

# Assignment Description: Calculate the most efficent way to make a amount using quarters, nickels, dimes, pennies


quarter = 25
dime = 10
nickel = 5
penny = 1

amount_str = input("Enter the amount in dollars (two decimals): ")

# Validate format (must contain exactly 2 decimal places)
if "." not in amount_str or len(amount_str.split(".")) != 2 or len(amount_str.split(".")[1]) != 2:
    print("Error: Please enter an amount with exactly two decimal places (example: 56.78)")
    exit()

# Convert "dollars.cents" into total cents
dollars, cents = amount_str.split(".")
amount = int(dollars) * 100 + int(cents)

# Calculate coins
quarters = amount // 25
amount %= 25

dimes = amount // 10
amount %= 10

nickels = amount // 5
amount %= 5

pennies = amount

# Output
print(f"{quarters} quarters,")
print(f"{dimes} dimes,")
print(f"{nickels} nickels,")
print(f"and {pennies} pennies to make ${amount_str}.")
