from abc import ABC, abstractmethod
from .plot import GraphWithWidgets


class Slide(ABC):
    @abstractmethod
    def render():
        pass


class GraphWithWidgetsSlide(Slide, GraphWithWidgets):
    def render(self):
        self.display()
