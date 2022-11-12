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
    openfile = open('results.txt', 'w', encoding="utf8") #UTF-8 is the default coding
    write_result_to_file(number_of_scores, openfile)
    openfile.close()
    results_file = open('results.txt', 'r', encoding="utf8")
    print(results_file.read())


def write_result_to_file(number_of_scores, openfile):
    """Save the scores to a file"""
    for score in range(number_of_scores):
        score = random.randint(0, 100)
        openfile.write(str(score) + " is " + score_status(score) + "\n")


def score_status(score):
    """Determine score status"""
    if 90 <= score <= 100:
        return "Excellent"
    if 50 <= score < 90:
        return "Passable"
    return "Bad"


main()
