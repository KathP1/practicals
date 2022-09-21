"""
Various for loops
"""


for i in range(1, 21, 2):
    print(i, end=' ')
print('\n')
for i in range(0, 100, 10):
    print(i, end=' ')
print('\n')
for i in range(20, 1, -1):
    print(i, end=' ')
print('\n')
number_of_stars = int(input("How many stars?:"))
for i in range(number_of_stars):
    print('*', end='')
print('\n')
row_length = 1
for i in range(number_of_stars):
    for j in range(row_length):
        print("*", end='')
    row_length = row_length + 1
    print()
