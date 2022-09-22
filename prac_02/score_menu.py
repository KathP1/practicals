"""Complete program, following structure.
Menu:
G - get a valid (0 - 100) score
P - print result
S - print as many stars as the score
Q - quit
"""

from math import floor


def main():
    score = -1  #If option P is selected before G this will trigger an error message
    MENU = """G - get score
P - print result
S - print as many stars as the score
Q - quit
    """
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
    for i in range(floor(score)):
        print('*', end='')


def score_status(score):
    if 90 <= score <= 100:
        print("A score of", score, "is Excellent")
    elif 50 <= score < 90:
        print("A score of", score, "is Passable")
    elif 0 <= score < 50:
        print("A score of", score, "is Bad")
    else:
        print("Get score first")


def get_valid_score():
    score = float(input("Enter score: "))
    while score == "" or score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


main()
