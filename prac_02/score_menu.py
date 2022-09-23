"""Complete program, following structure.
Menu:
G - get a valid (0 - 100) score
P - print result
S - print as many stars as the score
Q - quit

Help on empty user input from: https://stackoverflow.com/questions/19579997/how-to-catch-empty-user-input-using-a-try-and-except-in-python
"""

from math import floor

MENU = """G - get score 
P - print result
S - print as many stars as the score
Q - quit
"""


def main():
    """Get score, print result, print stars"""
    score = -1  # Trigger an error message if P is selected before G
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score: float = get_valid_score()
        elif choice == "P":
            score_status(score)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print("\n")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def print_stars(score):
    """Print as many stars as the score. Round down to integer"""
    try:
        if score:  # Score entered as a float
            for i in range(floor(score)):
                print('*', end='')
        if not score:  # Score not entered as float or is empty
            raise ValueError()
    except ValueError:
        print("Enter score first")


def score_status(score):
    """Determine score status"""
    try:
        if score:  # Score entered as a float
            if 90 <= score <= 100:
                print("A score of", score, "is Excellent")
            elif 50 <= score < 90:
                print("A score of", score, "is Passable")
            elif 0 <= score < 50:
                print("A score of", score, "is Bad")
            else:
                print("Get score first")
        if not score:  # Score not entered as float or is empty
            raise ValueError()
    except ValueError:
        print("Get score first")


def get_valid_score():
    """Get score and error check the score"""
    try:
        score = float(input("Enter score: "))
        if score:  # Score is entered as a float
            while score < 0 or score > 100:
                print("Invalid score")
                score = float(input("Enter score: "))
            return score
        if not score:  # Score not entered as float or is empty
            raise ValueError()
    except ValueError:
        print("Invalid value")


main()
