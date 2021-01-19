class SubsystemA:
    def operation_a(self) -> str:
        return "Operation a from subsystem A"

    def operation_b(self) -> str:
        return "Operation b from subsystem A"


class SubsystemB:
    def operation_a(self) -> str:
        return "Operation a from sybsystem B"

    def operation_b(self) -> str:
        return "Operation b from sybsystem B"


class Facade:
    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()

    def operation_a(self) -> str:
        return f"{self._subsystem_a.operation_a()} - " \
               f"{self._subsystem_b.operation_a()}"

    def operation_b(self) -> str:
        return f"{self._subsystem_a.operation_b()} - " \
               f"{self._subsystem_b.operation_b()}"


if __name__ == '__main__':
    facade = Facade()
    print(facade.operation_a())
    print(facade.operation_b())
