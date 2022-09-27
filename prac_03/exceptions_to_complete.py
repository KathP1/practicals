"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
Write a program that gets an integer from the user
and does not crash when a non-number is entered.
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Invalid (not an integer)")
print("Valid result is:", result)

# From Programming Patterns:
# is_valid_input = False
# while not is_valid_input:
#     try:
#         age = int(input("Age: "))
#         if age < 0:
#             print("Age must be >= 0")
#         else:
#             is_valid_input = True
#     except ValueError:
#         print("Invalid (not an integer)")
# print("Next year you will be", age + 1)
