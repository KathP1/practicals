"""
Menus
Create a very simple menu-driven program according to the given pseudocode
"""

name = input("Enter name: ")

MENU = """(H)ello
(G)oodbye
(Q)uit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")
