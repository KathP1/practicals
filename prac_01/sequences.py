"""
Menu driven number sequence generator
"""

"""Different number sequences"""

MENU = """E - Even numbers from x to y
O - Odd numbers from x to y
S - Squares from x to y
Q - Quit
"""
print(MENU)
choice = input(">>> ").upper()

starting_value = int(input("Enter the starting value, x: "))
ending_value = int(input("Enter the ending value, y: "))

while choice != "Q":
    if choice == "E":
        if starting_value % 2 == 0:
            for i in range(starting_value, ending_value + 1, 2):
                print(i, end=' ')
        else:
            for i in range(starting_value, ending_value, 2):
                print(i + 1, end=' ')
    elif choice == "O":
        if starting_value % 2 == 1:
            for i in range(starting_value, ending_value + 1, 2):
                print(i, end=' ')
        else:
            for i in range(starting_value, ending_value, 2):
                print(i + 1, end=' ')
    elif choice == "S":
        for i in range(starting_value, ending_value+1):
            print(i ** 2, end=' ')
    else:
        print("Invalid Option")
        print("\n")
        print(MENU)
        choice = input(">>> ").upper()
    print("\n")
    print(MENU)
    choice = input(">>> ").upper()
    starting_value = int(input("Enter the starting value, x: "))
    ending_value = int(input("Enter the ending value, y: "))
print("Thank you")
