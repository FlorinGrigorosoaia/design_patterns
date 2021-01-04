from threading import Lock, Thread


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    pass


def test_singleton(thread_number: int) -> None:
    print(f"Thread #{thread_number}:", id(Singleton()))


if __name__ == '__main__':
    first_thread = Thread(target=test_singleton, args=(0,))
    second_thread = Thread(target=test_singleton, args=(1,))

    first_thread.start()
    second_thread.start()

    first_thread.join()
    second_thread.join()
