"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "My Car")

    # Create a new Car object called "limo" that is initialised with 100 units of fuel.
    limo = Car(100, "Limo")
    # Add 20 more units of fuel to this new car object using the add method
    limo.add_fuel(20)
    # Print the amount of fuel in the car
    print(f"Amount of fuel in the car: {limo.fuel}")
    # Attempt to drive the car 115 km using the drive method.
    limo.drive(115)
    print(limo)
main()