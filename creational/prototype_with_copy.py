from copy import copy, deepcopy
from typing import Optional, Type


class Rectangle:
    def __init__(self, width: int, height: int, details: list) -> None:
        self._width = width
        self._height = height
        self._details = details

    def __copy__(self) -> Optional[Type["Rectangle"]]:
        copied_rectangle = self.__class__(
            self._width,
            self._height,
            copy(self._details)
        )
        copied_rectangle.__dict__.update(self.__dict__)

        return copied_rectangle

    def __deepcopy__(self, memodict=None) -> Optional[Type["Rectangle"]]:
        copied_rectangle = self.__class__(
            self._width,
            self._height,
            deepcopy(self._details)
        )
        copied_rectangle.__dict__ = deepcopy(self.__dict__)

        return copied_rectangle

    def __str__(self) -> str:
        return f"{self._width} {self._height} {self._details}"

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def details(self) -> list:
        return self._details

    def add_detail(self, detail: str) -> None:
        self._details.append(detail)


if __name__ == '__main__':
    original_rectangle = Rectangle(2, 4, ["red", "small"])
    shallow_copy_rectangle = copy(original_rectangle)
    deep_copy_rectangle = deepcopy(original_rectangle)

    print(original_rectangle)
    print(shallow_copy_rectangle)
    print(deep_copy_rectangle)

    original_rectangle.add_detail("nice")

    print(original_rectangle)
    print(shallow_copy_rectangle)
    print(deep_copy_rectangle)
