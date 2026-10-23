# Jenni VerBerkmoes
# 10/23/2026
# P4HW2
# Building on P3HW2 calculate gross pay for multiple employees, determined by user, and also calculates total amount paid for overtime, total amount paid for regular pay and total amount paid for all employees.

# Request input from user

name = input("Enter employee's name or done to terminate: ")

# Create accumulater variables for regular pay, overtime pay, gross pay and employee count
overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

while name != "done":
    # Add employee count plus 1
    employee_count += 1
    # Ask for employee info
    hours = float(input("How many hours did "  +name+   " work this week? "))
    rate = float(input("What is " +name+ "'s hourly pay rate? "))

    
# Calculate pay

    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_pay = 0
        overtime_hours = 0
        regular_pay = hours * rate
        gross_pay = regular_pay

    # Add to accumulator totals
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay

    # Display results to user
    print("--------------------------------------")
    print(f"Employee Name: {name:<30}")
    print()
    print("Hours worked      Pay Rate      Overtime      Overtime pay      RegHour Pay      Gross Pay")
    print("-------------------------------------------------------------------------------------------")
    print(f"{hours:.2f}{rate:18.2f}{overtime_hours:13.2f}{overtime_pay:16.2f}{regular_pay:18.2f}{gross_pay:17.2f}")
    
    print()

    name = input("Enter employee's name or done to terminate: ")

print()

print("Total number of employees entered: ", employee_count)
print("Total amount paid for overtime: $", format(overtimepay_total, ',.2f'))
print("Total amount paid for regular time: $", format(regularpay_total, ',.2f'))
print("Total amount paid in gross: $", format(grosspay_total, ',.2f'))