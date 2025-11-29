 # Adam Jones

 # Dat28 NOV 2025

  # P4HW2 - Payroll Summary

  # This program processes payroll information for multiple employees and provides a summary.






# Initialize totals
total_employees = 0
total_regular_pay = 0
total_overtime_pay = 0
total_gross_pay = 0

name = input("Enter employee's name (or type 'Done' to exit): ")

while name.lower() != "done":

    # Input regular hours
    regular_hours = float(input("Enter regular hours worked: "))

    # Allow $ sign in pay rate
    pay_rate_input = input("Enter regular pay rate (e.g. 15.50 or $15.50): ")
    pay_rate = float(pay_rate_input.replace("$", "").strip())

    # Calculate regular pay
    regular_pay = regular_hours * pay_rate

    # Input overtime hours and overtime pay
    overtime_hours = float(input("Enter overtime hours worked: "))
    overtime_pay_input = input("Enter overtime pay (e.g. 100.50 or $100.50): ")
    overtime_pay = float(overtime_pay_input.replace("$", "").strip())

    # Gross pay
    gross_pay = regular_pay + overtime_pay

    # Update totals
    total_employees += 1
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay

    # Format numbers
    regular_pay_f = f"${regular_pay:.2f}"
    overtime_pay_f = f"${overtime_pay:.2f}"
    gross_pay_f = f"${gross_pay:.2f}"
    pay_rate_f = f"${pay_rate:.2f}"

    # Print Pay Stub
    print("\n================= PAY STUB =================")
    print(f"Employee Name:        {name}")
    print("--------------------------------------------")
    print(f"Regular Hours:        {regular_hours:.2f}")
    print(f"Overtime Hours:       {overtime_hours:.2f}")
    print(f"Pay Rate:             {pay_rate_f}/hour")
    print(f"Regular Pay:          {regular_pay_f}")
    print(f"Overtime Pay:         {overtime_pay_f}")
    print("--------------------------------------------")
    print(f"Gross Pay:            {gross_pay_f}")
    print("============================================\n")

    # Ask for next employee
    name = input("Enter employee's name (or type 'Done' to exit): ")

# Payroll summary
print("\n================= PAYROLL SUMMARY =================")
print(f"Total Employees Entered:        {total_employees}")
print(f"Total Regular Pay:              ${total_regular_pay:.2f}")
print(f"Total Overtime Pay:             ${total_overtime_pay:.2f}")
print(f"Total Gross Pay:                ${total_gross_pay:.2f}")
print("===================================================")