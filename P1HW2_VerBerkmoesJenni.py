 # Jenni VerBerkmoes
 # 9/7/26
 # P1HW2
 # Use basic math to calculate travel expenses

print("This program calculates and displays travel expenses")
print()

#Program will prompt user to enter an intial budget amount for travel expenses and thier travel destination.

base = int(input("Enter budget: "))
print()
destination = input("Enter your travel destination: ")
print()

#program will prompt user to enter various travel expense amounts and will subtract those 
#amounts from the initial budget to get a remaining budget amount

num1 = int(input("How much do you think you will spend on gas? "))
print()
num2 = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
num3 = int(input("Last, how much do you need for food? "))

print("--------Travel Expenses--------")
print()

print("Location:", destination)
print("Initial budget:", base)
print()

print("Fuel:", num1)
print("Accomodation:", num2)
print("Food:", num3)
print()

final_result = base - num1 - num2 - num3
print("Remaining Balance:", final_result)
