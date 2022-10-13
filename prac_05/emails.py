"""
Emails
Estimate: 45 minutes
Actual:
"""


def main():
    """Create a dictionary of emails and names"""
    email_to_name = {}
    email = input("Email: ")

    while email != "":
        name = get_name_from_email(email)
        name_is_correct = input(f"Is your name {name}? (Y/n) ").lower()
        if name_is_correct == 'n':
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract the presumed name from the first part of the email address"""
    whole_name = email.split("@")[0]
    name_parts = whole_name.split(".")
    name = " ".join(name_parts).title()
    return name


main()
