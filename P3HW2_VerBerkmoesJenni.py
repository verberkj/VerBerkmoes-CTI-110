# Jenni VerBerkmoes
# 10/3/26
# P3HW2
# Create a program that will display to the user, based on user input, what thier overtime pay, regular pay and gross pay amounts are

# Request input from user

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculate if overtime hours were worked

overtime_hours = hours - 40.00


# Calculate overtime pay, if any

if hours > 40:
    overtime_pay = overtime_hours * (pay_rate * 1.5)
   

# Calculate regular pay

reg_pay = hours * pay_rate


# Calculate gross pay

gross_pay = overtime_pay + reg_pay

# Display results to user
print("--------------------------------------")
print(f"Employee Name: {name:<30}")
print()
print("Hours worked      Pay Rate      Overtime      Overtime pay      RegHour Pay      Gross Pay")
print("-------------------------------------------------------------------------------------------")
print(f"{hours:.2f}{pay_rate:18.2f}{overtime_hours:13.2f}{overtime_pay:16.2f}{reg_pay:18.2f}{gross_pay:17.2f}")