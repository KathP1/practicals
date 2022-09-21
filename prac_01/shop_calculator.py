"""
A program to work out the total price for a number of items
The program allows the user to enter the number of items and the price of each ifferent item.
The program computes the total price of those items
If the total price is over $100, then a 10% discount is applied to that total
Display the total

Error checking - if the number of items is less than zero, the message 'Invalid number of items!' should be displayed
and this quantity must be re-entered by the user until it is valid
"""

""" Program to calculate total price of items"""
total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price = total_price + price_of_item
    if total_price > 100:
        total_price = total_price - (total_price * 0.1)
print("Total price for", number_of_items, "items is ${:.2f}".format(total_price))
