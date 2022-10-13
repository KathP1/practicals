"""
Emails
Estimate: 45 minutes
Actual:
"""

email_to_name = {}
email = input("Email: ")
while email != "":
    whole_name = email.split("@")[0]
    name_parts = whole_name.split(".")
    name = " ".join(name_parts).title()
    email_to_name[email] = name
    print(email_to_name)
    name_is_correct = input(f"Is your name {name}? (Y/n) ").lower()
    if name_is_correct == 'n':
        correct_name = input("Name: ")
        email_to_name[email] = correct_name
    email = input("Email: ")
for email, name in email_to_name.items():
    print(f"{name} ({email})")
