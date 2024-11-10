from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def update(self, data) -> None:
        pass

class Observable(metaclass=ABCMeta):

    def __init__(self) -> None:
        self.observers = []  # инициализация списка наблюдателей
        super().__init__()

    def register_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def notify_observers(self, data) -> None:
        for observer in self.observers:
            observer.update(data)
