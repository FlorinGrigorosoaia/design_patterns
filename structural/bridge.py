from abc import ABC, abstractmethod


class Device(ABC):
    """
    The Implementation/Platform class.
    """
    def __init__(self):
        self._volume = 0
        self._enabled = False

    @abstractmethod
    def is_enabled(self) -> bool:
        pass

    @abstractmethod
    def enable(self) -> None:
        pass

    @abstractmethod
    def disable(self) -> None:
        pass

    @abstractmethod
    def get_volume(self) -> int:
        pass

    @abstractmethod
    def set_volume(self, percentage: int) -> None:
        pass


class TV(Device):
    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self) -> None:
        self._enabled = True

    def disable(self) -> None:
        self._enabled = False

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, percentage: int) -> None:
        if self._enabled:
            self._volume = percentage


class Radio(Device):
    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self) -> None:
        self._enabled = True

    def disable(self) -> None:
        self._enabled = False

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, percentage: int) -> None:
        self._volume = percentage


class RemoteControl:
    """
    The Abstraction/Domain/Infrastructure class.
    """
    def __init__(self, device: Device):
        self._device = device

    def toggle_power(self) -> None:
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()

    def volume_down(self, volume_difference: int = 5) -> None:
        self._device.set_volume(self._device.get_volume() - volume_difference)

    def volume_up(self, volume_difference: int = 5) -> None:
        self._device.set_volume(self._device.get_volume() + volume_difference)


if __name__ == '__main__':
    tv = TV()
    remote = RemoteControl(tv)

    print(tv.get_volume())
    remote.toggle_power()
    remote.volume_up()
    print(tv.get_volume())
