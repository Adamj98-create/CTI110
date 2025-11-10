# Adam Jones
# 6-NOV-2025
# Assignment NameP1HW2
# A
# This assignment is making a program to build a budget for vacation

print("This program calculates and displays travel expenses")
destination = input("destination: ")
budget = float(input("budget: "))
gasmoney = float(input("gas: "))
accommodation = float(input("accommodation: "))
food = float(input("food: "))
remaining_balance = budget - (gasmoney + accommodation + food)


print("----------Travel Expenses----------")
print("destination:", f"{destination}")
print("Budget:", f"${budget:.2f}",)
print("Gas:",f"${gasmoney:.2f}",)
print("Accommodation:",f"${accommodation:.2f}",)
print("Food:", f"${food:.2f}")
print("===================================")




print("Remaining Balance:", f"${remaining_balance:.2f}")






