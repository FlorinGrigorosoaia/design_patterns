class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    pass


if __name__ == '__main__':
    first = Singleton()
    second = Singleton()

    print(id(first), id(second), id(first) == id(second))
