from abc import abstractmethod
from multimethod import multimethod


class ShapePrototype:
    @multimethod
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    @__init__.register
    def __init__(self, prototype: "ShapePrototype") -> None:
        self._x = prototype.x
        self._y = prototype.y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @abstractmethod
    def clone(self) -> "ShapePrototype":
        pass


class Rectangle(ShapePrototype):
    @multimethod
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__(x, y)

        self._width = width
        self._height = height

    @__init__.register
    def __init__(self, prototype: "Rectangle") -> None:
        super().__init__(prototype)

        self._width = prototype.width
        self._height = prototype.height

    def __str__(self) -> str:
        return f"{self._x} {self._y} {self._width} {self._height}"

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def clone(self) -> ShapePrototype:
        return Rectangle(self)


if __name__ == '__main__':
    original_rectangle = Rectangle(1, 1, 4, 8)
    cloned_rectangle = original_rectangle.clone()

    print(original_rectangle)
    print(cloned_rectangle)
