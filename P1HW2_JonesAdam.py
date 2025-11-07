# Adam Jones
 # 6-NOV-2025
 # Assignment NameP1HW2
 # A 
# This assignment is making a program to build a budget for vacation

print("This program calculates and siplays travel expenses")
budget = float(input("Enter your budget for the trip: "))
destination = input("Enter your travel destination: ")
gasmoney = float(input("Enter amount estimated amount for gas: "))
accommodation = float(input("Enter the cost of accomodation/hotel: "))
food = float(input("Enter the cost of food: "))
remaining_balance = budget - (gasmoney + accommodation + food)
2
print("----------Travel Expensed----------")
print("Location:", budget)
print("Budget:", destination)
print("Estimated Gas Cost:", gasmoney)
print("Estimated Accomodation/Hotel Cost:", accommodation)
print("Estimated Food Cost:", food)

print("Remaining Balance:", remaining_balance)


