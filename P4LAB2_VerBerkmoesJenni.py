# Jenni VerBerkmoes
# 10/20/2026
# P4LAB2
# Use while loop and for loop together



# Set a variable for determining if program needs to run again after executing

run_again = "yes"

while run_again != "no":

    # Get integer from user
    user_num = int(input("Enter an integer: "))

    # If user entered a positive integer, display multiplication table for that value and range (1-12)
    if user_num >= 0:
        for item in range (1, 13):
            
            #Print results for user
            print(f"{user_num} * {item} = {user_num * item}")

    # If user entered a negative integer, display message to user
    else: 
        print("This program does not handle negative values.")

# Ask user to run program again
    run_again = input("Would you like to run this program again? ")

# If user answers no, program ends and displays statement to user
print("Program is ending....")
