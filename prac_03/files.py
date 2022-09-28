"""Do-from-scratch Exercises"""

"""1. Write code that asks the user for their name
then opens a file called 'name.txt'
and writes that name to it.
Remember to close your file"""

# FILE_NAME = "name.txt"
#
# user_name = input("What is your name? ")
# out_file = open(FILE_NAME, 'w')
# print(user_name, file=out_file)
# out_file.close()

"""Write code that opens "name.txt"
and reads the name
then prints "Your name is (whatever the name is)"""

# in_file = open(FILE_NAME, 'r')
# name = in_file.read()
# print(f"Your name is {name}")
# in_file.close()

"""Create a file called 'numbers.txt'
and save it in your prac directory.
Put the following three numbers on separate lines
in the file and save it: 17, 42, 400
Write code that opens "numbers.txt"
reads only the first two numbers and adds them together
then prints the result, which should be 59"""

FILE_NAME = "numbers.txt"
out_file = open(FILE_NAME, 'w')
print(f"17\n42\n400\n", file=out_file)
out_file.close()


in_file = open(FILE_NAME, 'r')
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
print(number_1 + number_2)
in_file.close()



