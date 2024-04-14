import random
from prac_09.car import Car

class UnreliableCar(Car):
    """A Car that may or may not drive based on reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability