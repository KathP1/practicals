"""
CP1404 Practical 09
Testing unreliable car class
"""

from prac_09.unreliable_car import UnreliableCar

# 1. Create a new UnreliableCar object
my_unreliable_car = UnreliableCar("Prius 1", 100, 50)
print(my_unreliable_car)

# # 2. Drive the unreliable_car 40km
my_unreliable_car.drive(40)


# 3. Print the unreliable car's details and the distance travelled
print(my_unreliable_car)


