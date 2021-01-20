import json


class Flyweight:
    def __init__(self, shared_state: list) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: list) -> None:
        print(f"Flyweight: displaying shared ({json.dumps(self._shared_state)}) state "
              f"and unique ({json.dumps(unique_state)}) state.")


class FlyweightFactory:
    def __init__(self, initial_flyweights: dict) -> None:
        self._flyweights_cache = dict()

        for state in initial_flyweights:
            self._flyweights_cache[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: dict) -> str:
        return "_".join(sorted(state))

    def get_flyweight(self, state: dict) -> Flyweight:
        key = self.get_key(state)

        if key not in self._flyweights_cache:
            self._flyweights_cache[key] = Flyweight(state)
        return self._flyweights_cache[key]

    def list_flyweights(self) -> None:
        print(f"FlyweightFactory: I have {len(self._flyweights_cache)} flyweights:")
        print("\n".join(map(str, self._flyweights_cache.keys())))


def add_car_to_police_database(factory: FlyweightFactory,
                               plates: str, owner: str,
                               brand: str, model: str, color: str) -> None:
    flyweight = factory.get_flyweight([brand, model, color])
    flyweight.operation([plates, owner])


if __name__ == '__main__':
    initial_factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"]
    ])
    initial_factory.list_flyweights()

    add_car_to_police_database(initial_factory, "CL234IR", "James Doe", "BMW", "M5", "red")
    add_car_to_police_database(initial_factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    initial_factory.list_flyweights()
