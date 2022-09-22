"""
Program to determine score status and print to txt file
"""

import random


def main():
    """Print test results to text file"""
    number_of_scores = int(input("Number of scores: "))
    while number_of_scores < 0:
        print("Invalid number of scores!")
        number_of_scores = int(input("Number of scores: "))
    openfile = open('results.txt', 'w')
    for i in range(number_of_scores):
        score = random.randint(0, 100)
        x = str(score)
        # print(score, "is", score_status(score))
        openfile.write(str(score) + " is " + score_status(score) + "\n")
    openfile.close()
    results_file = open('results.txt', 'r')
    print(results_file.read())


def score_status(score):
    """Determine score status"""
    if 90 <= score <= 100:
        return "Excellent"
    elif 50 <= score < 90:
        return "Passable"
    elif 0 <= score < 50:
        return "Bad"
    else:
        return "Invalid score"


main()
