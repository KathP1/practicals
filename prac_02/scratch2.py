"""Complete program, following structure.
Menu:
G - get a valid (0 - 100) score
P - print result
S - print as many stars as the score
Q - quit
"""

from math import floor


def main():
    MENU = """G - get score
P - print result
S - print as many stars as the score
Q - quit
    """
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score: int = get_valid_score()
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
    else:
        print("A score of", score, "is Bad")


def get_valid_score():
    score = int(input("Enter score: "))
    while score == "":
        print('Invalid Input')
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


main()
