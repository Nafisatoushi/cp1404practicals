from prac_09.unreliable_car import UnreliableCar

# Create an unreliable car with name, fuel, and reliability
my_car = UnreliableCar("Mostly Good", 100, 90)
my_dodgy_car = UnreliableCar("Dodgy", 100, 9)

# Attempt to drive the cars for different distances
for distance in range(1, 12):
    print(f"Attempting to drive {distance}km:")
    distance_driven = my_car.drive(distance)
    print(f"{my_car.name} drove {distance_driven}km")
    distance_driven = my_dodgy_car.drive(distance)
    print(f"{my_dodgy_car.name} drove {distance_driven}km")

# Print the final state of the cars
print(my_car)
print(my_dodgy_car)