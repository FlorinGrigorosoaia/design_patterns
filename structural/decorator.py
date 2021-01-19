from abc import abstractmethod


class Notifier:
    @abstractmethod
    def notify(self) -> None:
        pass


class SimpleNotifier(Notifier):
    def notify(self) -> None:
        print("Here is a simple notification.")


class NotifierDecorator(Notifier):
    def __init__(self, notifier: Notifier):
        self._notifier = notifier

    @property
    def notifier(self) -> Notifier:
        return self._notifier

    def notify(self) -> None:
        self._notifier.notify()


class SlackDecorator(NotifierDecorator):
    def __init__(self, notifier: Notifier):
        super().__init__(notifier)

    def notify(self) -> None:
        super().notify()
        print("Here is a Slack notification.")


class FacebookDecorator(NotifierDecorator):
    def __init__(self, notifier: Notifier):
        super().__init__(notifier)

    def notify(self) -> None:
        super().notify()
        print("Here is a Facebook notification.")


if __name__ == '__main__':
    notifier_stack = SimpleNotifier()
    notifier_stack.notify()
    print()

    notifier_stack = SlackDecorator(notifier_stack)
    notifier_stack.notify()
    print()

    notifier_stack = FacebookDecorator(notifier_stack)
    notifier_stack.notify()
