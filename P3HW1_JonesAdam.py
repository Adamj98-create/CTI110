# I was supposed to put a comment here
# Adam Jones
# P3HW1
# This program takes a number grade, determines average and displays letter grade
# for average.
# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))
# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# determine lowest, highest, sum and average for grades
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)
# determine letter grade for average
if average >= 90:
	letter = 'A'
elif average >= 80:
	letter = 'B'
elif average >= 70:
	letter = 'C'
elif average >= 60:
	letter = 'D'
else:
	letter = 'F'

print(f'Lowest grade: {lowest}')
print(f'Highest grade: {highest}')
print(f'Sum of grades: {total}')
print(f'Average grade: {average:.2f}')
print(f'Your grade is: {letter}')
