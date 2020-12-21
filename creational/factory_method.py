from abc import ABC, abstractmethod

import platform


class Button(ABC):
    @abstractmethod
    def render(self) -> None:
        pass


class WindowsButton(Button):
    def render(self) -> None:
        print("Rendering WindowsButton!")


class LinuxButton(Button):
    def render(self) -> None:
        print("Rendering LinuxButton")


class Dialog(ABC):
    """
    Creator class
    """
    @abstractmethod
    def create_button(self) -> Button:
        pass

    def render(self) -> None:
        self.create_button().render()


class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()


class LinuxDialog(Dialog):
    def create_button(self) -> Button:
        return LinuxButton()


if __name__ == '__main__':
    """
    Client code
    """
    dialog = WindowsDialog() if platform.system() == "Windows" else LinuxDialog()
    dialog.render()
