# Jenni VerBerkmoes
# 9/21/26
# P2LAB2
# Using Dictionaries

cars = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado': 26}

#Created a variable
keys = cars.keys()

#Get keys from the dictionary
print(keys)

#Get a car from the user
car_name = input("Enter a vehicle to see it's MPG: ")

#Get MPG for the given car
car_mpg = cars[car_name]

print(f"The {car_name} gets {car_mpg} mpg.")

#Get miles from user
miles_driven = float(input(f"How many miles will you drive the {car_name}? "))

#Calculate the gallons of gas needed to drive the specified vehicle the given number of miles.
gallons_needed = miles_driven/car_mpg

#Display results
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles.")