# Jenni VerBerkmoes
# 10/3/26
# P3HW1
# This program takes a number grade, determines average and displays letter grade for average.


# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest , sum and average for grades

import math

low = min(grades)
high = max(grades)
sum = (math.fsum(grades))
avg = (sum/6)

print()
# Print results for user
print('--------------Results---------------')
print(f'{"Lowest Grade:":<15}{low}')
print(f'{"Highest Grade:":<15}{high}')
print(f'{"Sum of Grades:":<15}{sum}')
print(f'{"Average:":<15}{avg:.2f}')
print('-------------------------------------')


# Determine letter grade for average

if avg >= 90:
    print('Your grade is: A')

elif avg >= 80:
    print('Your grade is: B')

elif avg >= 70:
    print('Your grade is: C')

elif avg >= 60:
    print('Your grade is: D')

else:
    print('Your grade is: F') 





