"""
CP1404 Practical 09
Testing taxi class
"""

from prac_09.taxi import Taxi

# 1. Create a new taxi object
my_taxi = Taxi("Prius 1", 100)

# 2. Drive the taxi 40km
my_taxi.drive(40)

# 3. Print the taxi's details and the current fare
print(f"{my_taxi}, current fare: ${my_taxi.get_fare():.2f}")

# 4. Restart the meter and then drive the car 100 km
my_taxi.start_fare()
my_taxi.drive(100)

# 5. Print the details and the current fare
# Note: taxi couldn't drive 100km because there was only 60 units of fuel left
print(f"{my_taxi}, current fare: ${my_taxi.get_fare():.2f}")
