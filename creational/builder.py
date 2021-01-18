from abc import ABC, abstractmethod
from typing import Union


class Car:
    """
    The actual product
    """
    def __init__(self):
        self._engine = None
        self._wheels = None
        self._windows = None

    @property
    def engine(self) -> Union[str, None]:
        return self._engine

    @engine.setter
    def engine(self, engine: str) -> None:
        self._engine = engine

    @property
    def wheels(self) -> Union[int, None]:
        return self._wheels

    @wheels.setter
    def wheels(self, wheels: int) -> None:
        self._wheels = wheels

    @property
    def windows(self) -> Union[int, None]:
        return self._windows

    @windows.setter
    def windows(self, windows: int) -> None:
        self._windows = windows

    def __str__(self):
        return f"Engine: {self._engine}\n" \
               f"Wheels: {self._wheels}\n" \
               f"Windows: {self._windows}"


class Builder(ABC):
    """
    Builder interface
    """
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def build_engine(self, engine) -> None:
        pass

    @abstractmethod
    def build_wheels(self, wheels) -> None:
        pass

    @abstractmethod
    def build_windows(self, windows) -> None:
        pass


class CarBuilder(Builder):
    """
    Concrete Builder
    """
    def __init__(self):
        self._product = None

        self.reset()

    def reset(self) -> None:
        self._product = Car()

    @property
    def product(self) -> Car:
        product = self._product
        self.reset()
        return product

    def build_engine(self, engine: str) -> None:
        self._product.engine = engine

    def build_wheels(self, wheels: int) -> None:
        self._product.wheels = wheels

    def build_windows(self, windows: int) -> None:
        self._product.windows = windows


class Director:
    def __init__(self, builder: Builder):
        self._builder = builder

    def build_minimum_product(self) -> None:
        self._builder.build_engine("new_engine")

    def build_full_product(self) -> None:
        self._builder.build_engine("new_engine")
        self._builder.build_wheels(4)
        self._builder.build_windows(6)


if __name__ == '__main__':
    """
    Client code
    """
    car_builder = CarBuilder()
    director = Director(car_builder)

    director.build_minimum_product()
    print(car_builder.product)

    director.build_full_product()
    print(car_builder.product)
