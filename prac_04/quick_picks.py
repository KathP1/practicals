"""
A program that asks the user how many "quick picks they wish to generate
The program then generates than many lines of output.
Each line consists of 6 random numbers between 1 and 45
"""

import random

quick_pics = []
number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(6):
        number = random.randint(1, 45)
        if number in quick_pick:
            number = random.randint(1, 45)
        quick_pick.append(number)
    quick_pick.sort()
    print(' '.join(f"{number:2}" for number in quick_pick))
