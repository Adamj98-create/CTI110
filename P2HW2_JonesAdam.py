#Adam Jones

 #11/NOV/2025

 #P2HW2
 
 #A list of grades in module 1-5 with their averages

print("Scores for Smith fromn Module 1 to Module 5")

module1 = float(input("Enter Grade for Module 1: "))
module2 = float(input("Enter Grade for Module 2: "))
module3 = float(input("Enter Grade for Module 3: "))
module4 = float(input("Enter Grade for Module 4: "))
module5 = float(input("Enter Grade for Module 5: "))
grades = [module1, module2, module3, module4, module5]

print("-------Results-------")
print("Lowest grade:", f"{min(grades):<.1f}")
print("Highest Grade:", f"{max(grades):<.1f}")
print("Sum of Grades:", f"{sum(grades):<.1f}")
print("Average:", f"{sum(grades)/len(grades):<.2f}")
