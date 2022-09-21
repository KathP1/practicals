"""
Program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    score_status = determine_score_status(score)
    print(score_status)


def determine_score_status(score):
    if 90 <= score <= 100:
        return "Excellent"
    elif 50 <= score < 90:
        return "Passable"
    elif 0 <= score < 50:
        return "Bad"
    else:
        return "Invalid score"


main()
