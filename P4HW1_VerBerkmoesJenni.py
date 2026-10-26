# Jenni VerBerkmoes
# 10/23/2026
# P4HW1
# Create loops to request scores from user, create list to hold scores, and then display grade, average and lowest score to user


# Create empty list
score_list = []

# Ask user how many times they would like to enter a score
num_scores = int(input("How many scores do you want to enter? "))
print()

# Ask user for scores 
for counter in range(1, num_scores+1):
    score = float(input(f"Enter score #{counter}: "))

    # Check if score is valid (0 -100) and if not ask user to input score again
    while score < 0 or score > 100:
        print()
        print("INVALID score entered!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{counter} again: "))

    # Append valid scores to the list
    if score >= 0 and score <= 100:
        score_list.append(score)  
print()
    
# Find lowest grade in the list
lowest_grade = min(score_list)

# Remove lowest from the list to create a modified list
score_list.remove(lowest_grade)

# Get the sum of the list after removing the lowest grade
import math
sum = (math.fsum(score_list))

# Change the number of scores in the list to be one lower than what the user entered to account for the removal of the lowest grade
num_scores = num_scores - 1

# Find the average of the modified list
average = float(sum/num_scores)

# Find the letter grade of the average score in the modified list
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"


# Display Results to the user
print("------------Results------------")
print(f'{"Lowest Grade:":<20}{lowest_grade}')
print(f'{"Modified List:":<20}{score_list}')
print(f'{"Scores Average:":<20}{average:.2f}')
print(f'{"Grade:":<20}{grade}')
print("--------------------------------")


  


