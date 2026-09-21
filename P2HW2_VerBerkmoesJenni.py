#Jenni VerBerkmoes
#9/21/26
#P2HW2
#Create separate input statements that prompts the user to enter test grades, and then displays 
#various calculations

#Request test grades from user for modules 1 - 6

module_1 = float(input("Enter grade for module 1: "))
module_2 = float(input("Enter grade for module 2: "))
module_3 = float(input("Enter grade for module 3: "))
module_4 = float(input("Enter grade for module 4: "))
module_5 = float(input("Enter grade for module 5: "))
module_6 = float(input("Enter grade for module 6: "))
print()
#List of all test grades given by the user
test_grades = [{module_1}, {module_2}, {module_3}, {module_4}, {module_5}, {module_6}]

#Search list for lowest test grade
lowest_grade = min(module_1, module_2, module_3, module_4, module_5, module_6)

#Search list for lowest test grade
highest_grade = max(module_1, module_2, module_3, module_4, module_5, module_6)

#Calculate the sum of all grades
import math
sum_of_all_grades = (math.fsum([module_1, module_2, module_3, module_4, module_5, module_6]))

#Calculate the average of all grades
average = float(sum_of_all_grades/6)

#Display Results
print("------------Results------------")
print(f'{"Lowest Grade:":<20}{lowest_grade}')
print(f'{"Highest Grade:":<20}{highest_grade}')
print(f'{"Sum of Grades:":<20}{sum_of_all_grades}')
print(f'{"Average:":<20}{average:.2f}')
print("--------------------------------")


