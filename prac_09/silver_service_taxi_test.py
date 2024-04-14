# silver_service_taxi_test.py

from prac_09.silver_service_taxi import SilverServiceTaxi

# Create a SilverServiceTaxi with name, fuel, fanciness
my_silver_taxi = SilverServiceTaxi("Hummer", 200, 4)

# Drive the taxi for a certain distance
my_silver_taxi.drive(18)

# Print the details of the taxi using __str__ method
print(my_silver_taxi)
