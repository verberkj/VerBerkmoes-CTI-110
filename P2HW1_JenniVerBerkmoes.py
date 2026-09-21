#Jenni VerBerkmoes
#9/21/26
#P2HW1
#Changing how results are displayed from a previous assignment

print("This program calculates and displays travel expenses")
print()

#Program will prompt user to enter an intial budget amount for travel expenses and thier travel destination.

base = float(input("Enter budget: "))
print()
destination = input("Enter your travel destination: ")
print()

#program will prompt user to enter various travel expense amounts and will add all total expenses together
#and then subtract that total from the initial budget amount to get a remaining budget amount

num1 = float(input("How much do you think you will spend on gas? "))
print()
num2 = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()
num3 = float(input("Last, how much do you need for food? "))

print("----------Travel Expenses----------")
print()
print(f'{"Location:":<20}{destination}')
print(f'{"Initial budget:":<20}{"$"}{base:.2f}')

print(f'{"Fuel:":<20}{"$"}{num1:.2f}')
print(f'{"Accomodation:":<20}{"$"}{num2:.2f}')
print(f'{"Food:":<20}{"$"}{num3:.2f}')
print()
print("-----------------------------------")

total_expenses = num1 + num2 + num3
final_result = base - total_expenses
print(f"Remaining Balance: ${final_result:.2f}")