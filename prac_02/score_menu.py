"""Complete program, following structure.
Menu:
G - get a valid (0 - 100) score
P - print result
S - print as many stars as the score
Q - quit
"""
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
            score = int(input("Enter score: "))
            while score == "" or score < 0 or score > 100:
                print("Invalid score")
                score = int(input("Enter score: "))
        elif choice == "P":
            if 90 <= score <= 100:
                print("A score of", score, "is Excellent")
            elif 50 <= score < 90:
                print("A score of", score, "is Passable")
            else:
                print("A score of", score, "is Bad")
        elif choice == "S":
            for i in range(score):
                print('*', end='')
        else:
            print("Invalid choice")
        print("\n")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


main()
