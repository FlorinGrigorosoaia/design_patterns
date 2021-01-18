from abc import ABC, abstractmethod
from typing import List


class Product:
    @abstractmethod
    def get_cost(self) -> int:
        pass


class Box(Product):
    REGULAR_COST = 1

    def __init__(self):
        self._products = list()

    @property
    def products(self) -> List[Product]:
        return self._products

    def add_product(self, product: Product) -> None:
        self._products.append(product)

    def remove_product(self, product: Product) -> None:
        self._products.remove(product)

    def get_cost(self) -> int:
        return Box.REGULAR_COST + sum([
            product.get_cost()
            for product in self._products
        ])


class Shoes(Product):
    def __init__(self, cost: int):
        self._cost = cost

    def get_cost(self) -> int:
        return self._cost


class Sunglasses(Product):
    def __init__(self, cost: int):
        self._cost = cost

    def get_cost(self) -> int:
        return self._cost


if __name__ == '__main__':
    red_shoes_box = Box()
    red_shoes_box.add_product(Shoes(200))
    red_shoes_box.add_product(Shoes(350))
    print(f"Cost of red shoes box: {red_shoes_box.get_cost()}")

    blue_shoes_box = Box()
    blue_shoes_box.add_product(Shoes(180))
    blue_shoes_box.add_product(Shoes(400))
    blue_shoes_box.add_product(Shoes(250))
    print(f"Cost of blue shoes box: {blue_shoes_box.get_cost()}")

    sunglasses = Sunglasses(100)
    print(f"Cost of sunglasses: {sunglasses.get_cost()}")

    party_products = Box()
    party_products.add_product(Shoes(370))
    party_products.add_product(Sunglasses(170))
    print(f"Cost of party products box: {party_products.get_cost()}")

    all_products = Box()
    all_products.add_product(red_shoes_box)
    all_products.add_product(blue_shoes_box)
    all_products.add_product(sunglasses)
    all_products.add_product(party_products)
    print(f"Cost of all products box: {all_products.get_cost()}")
