class CelsiusThermometer:
    """
    The Target class (domain-specific for client code).
    """
    def __init__(self, celsius_degrees: float):
        self._celsius_degrees = celsius_degrees

    @property
    def celsius_degrees(self) -> float:
        return self._celsius_degrees


class FahrenheitThermometer:
    """
    The Adaptee class (incompatible with client code).
    """
    def __init__(self, fahrenheit_degrees: float):
        self._fahrenheit_degrees = fahrenheit_degrees

    @property
    def fahrenheit_degrees(self) -> float:
        return self._fahrenheit_degrees


class FahrenheitToCelsiusThermometerAdapter(CelsiusThermometer):
    """
    The Adapter (makes the Adaptee compatible with the Target required by client code).
    """
    def __init__(self, fahrenheit_thermometer: FahrenheitThermometer):
        super().__init__(
            (fahrenheit_thermometer.fahrenheit_degrees - 32) * 5 / 9
        )


def print_celsius_degrees(celsius_thermometer: CelsiusThermometer) -> None:
    """
    Client code.
    """
    print(celsius_thermometer.celsius_degrees)


if __name__ == '__main__':
    print_celsius_degrees(CelsiusThermometer(32))
    print_celsius_degrees(
        FahrenheitToCelsiusThermometerAdapter(FahrenheitThermometer(68))
    )
