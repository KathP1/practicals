"""
CP1404 Practical 09
Testing taxi class
"""

from prac_09.silver_service_taxi import SilverServiceTaxi

# 1. Create a new SilverServiceTaxi object
my_silver_service_taxi = SilverServiceTaxi("Hummer", 200, 2)
print(my_silver_service_taxi)

# 2. Drive the SilverServiceTaxi 18km
my_silver_service_taxi.drive(18)

# 3. Print the SilverServiceTaxi's details and the current fare
print(f"{my_silver_service_taxi}, current fare: ${my_silver_service_taxi.get_fare():.2f}")

