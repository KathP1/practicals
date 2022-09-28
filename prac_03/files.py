"""Do-from-scratch Exercises"""

"""1. Write code that asks the user for their name
then opens a file called 'name.txt'
and writes that name to it.
Remember to close your file"""

FILE_NAME = "name.txt"

user_name = input("What is your name? ")
out_file = open(FILE_NAME, 'w')
print(user_name, file=out_file)
out_file.close()

"""Write code that opens "name.txt"
and reads the name
then prints "Your name is (whatever the name is)"""

in_file = open(FILE_NAME, 'r')
name = in_file.read()
print(f"Your name is {name}")
in_file.close()


