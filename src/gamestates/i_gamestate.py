import abc


class IGameState(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def render(self, screen):
        pass

    @abc.abstractmethod
    def handle_events(self, event):
        pass