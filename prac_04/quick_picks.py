"""
A program that asks the user how many "quick picks they wish to generate
The program then generates than many lines of output.
Each line consists of 6 random numbers between 1 and 45
"""

import random

quick_pics = []
number_of_quick_picks = int(input("How many quick picks? "))
for number in range(number_of_quick_picks):
    quick_pick = []
    number = random.randint(1, 45)
    quick_pick.append(number)
    print(quick_pick)