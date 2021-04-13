from abc import abstractmethod


class ServiceInterface:
    @abstractmethod
    def operation(self) -> None:
        pass


class Service(ServiceInterface):
    def operation(self) -> None:
        print("Executing operation from Service")


class Proxy(ServiceInterface):
    def __init__(self):
        self._service = None

    def operation(self) -> None:
        print("Checking things in proxy")
        if self._service is None:
            self._service = Service()
        self._service.operation()


if __name__ == '__main__':
    proxy = Proxy()
    proxy.operation()
