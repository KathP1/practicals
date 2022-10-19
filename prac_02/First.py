"""
On paper, write a pgram that asks the user for a password,
with error-checking to repeat if the password doesn't meet minimum length
Print asterisks as long as the word
"""


def main():
    minimum_length = 8
    password = input("Password: ")
    while len(password) < minimum_length:
        print("Password must be a minimum of ", minimum_length, "characters.")
        password = input("Password: ")
    print('*' * len(password))


main()
