"""
Emails
Estimate: 45 minutes
Actual:
"""

email_to_name = {}
email = input("Email: ")
while email != "":
    suggested_name = email.split("@")[0].title()
    print(suggested_name)
    email = input("Email: ")
