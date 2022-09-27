"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("The denominator cannot equal 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")

# 1. When will a ValueError occur?
# When anything other than an integer is entered by the user
# at line 10 (numerator) or 11 (denominator)

# 2. When will a ZeroDivisionError occur?
# When user enters a 0 at line 11 (denominator)

# 3. Could you change the code to avoid the possibility of a
# ZeroDivisionError?
# Use an if statement to tell the user not to enter a )
# and to prompt them to reenter the denominator


