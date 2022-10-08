"""
A program that prompts the user for 5 numbers
stores each number in a list
output information about these numbers
"""

numbers = []

for number in range(1, 4):
    number = float(input(f"Enter number {str(number)}: "))
    numbers.append(number)
    # print(numbers)
for number in numbers:
    print(f"Number: {int(number)}")
print(f"The first number is {int(numbers[0])}")
print(f"The last number is {int(numbers[-1])}")
print(f"The smallest number is {int(min(numbers))}")
print(f"The largest number is {int(max(numbers))}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

"""Woefully inadequate security checker"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("What is your username?: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
