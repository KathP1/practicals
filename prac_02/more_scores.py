"""
Program to determine score status and write to txt file
"""

import random


def main():
    """Write test results to text file"""
    number_of_scores = int(input("Number of scores: "))
    while number_of_scores < 0:
        print("Invalid number of scores!")
        number_of_scores = int(input("Number of scores: "))
    openfile = open('results.txt', 'w')
    write_result_to_file(number_of_scores, openfile)
    openfile.close()
    results_file = open('results.txt', 'r')
    print(results_file.read())


def write_result_to_file(number_of_scores, openfile):
    for i in range(number_of_scores):
        score = random.randint(0, 100)
        openfile.write(str(score) + " is " + score_status(score) + "\n")


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
