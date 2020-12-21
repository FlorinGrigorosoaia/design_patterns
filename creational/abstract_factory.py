from abc import ABC, abstractmethod

import platform


class Button(ABC):
    @abstractmethod
    def click(self) -> None:
        pass


class WindowsButton(Button):
    def click(self) -> None:
        print("I have clicked the Windows button!")


class LinuxButton(Button):
    def click(self) -> None:
        print("I have clicked the Linux button!")


class CheckBox(ABC):
    @abstractmethod
    def check(self) -> None:
        pass


class WindowsCheckBox(CheckBox):
    def check(self) -> None:
        print("I have checked the Windows check box!")


class LinuxCheckBox(CheckBox):
    def check(self) -> None:
        print("I have checked the Linux check box!")


class UIElementsAbstractFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox:
        pass


class WindowsUIElementsFactory(UIElementsAbstractFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> CheckBox:
        return WindowsCheckBox()


class LinuxUIElementsFactory(UIElementsAbstractFactory):
    def create_button(self) -> Button:
        return LinuxButton()

    def create_checkbox(self) -> CheckBox:
        return LinuxCheckBox()


class Application:
    """
    Client code
    """
    def __init__(self, factory: UIElementsAbstractFactory):
        self._button = factory.create_button()
        self._checkbox = factory.create_checkbox()

    def run(self) -> None:
        self._button.click()
        self._checkbox.check()


if __name__ == '__main__':
    """
    Client code configuration
    """
    concrete_factory = WindowsUIElementsFactory() \
        if platform.system() == "Windows" \
        else LinuxUIElementsFactory()
    application = Application(concrete_factory)
    application.run()
