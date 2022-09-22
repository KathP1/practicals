"""
Program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    score_status = determine_score_status(score)
    print(score_status)
    print("\n")
    score = random.randint(0, 100)
    score_status = determine_score_status(score)
    print("The random score of", score, "is", score_status)


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
