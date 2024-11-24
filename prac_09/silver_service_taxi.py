from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A Silver Service Taxi, which is a specialized version of a Taxi."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness
