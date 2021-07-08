from abc import ABC, abstractmethod
from IPython.display import display
import ipywidgets
import matplotlib.pyplot as plt

# set the default figure size for plots
plt.rcParams["figure.figsize"] = (8, 4.5)


class GraphWithWidgets(ABC):
    DEBUG = False

    @abstractmethod
    def widgets(self):
        pass

    @abstractmethod
    def graph(self, out):
        pass

    @abstractmethod
    def on_update(self, *args, **kwargs):
        pass

    def add_axes_lines(self, ax):
        ax.grid(True, which="both")
        ax.axhline(y=0, color="k")
        ax.axvline(x=0, color="k")

    def display(self):
        left, widgets = self.widgets()
        right = ipywidgets.Output()

        display(
            ipywidgets.HBox(
                children=[left, right],
                layout=ipywidgets.Layout(display="flex", align_items="center"),
            ),
        )

        with right:
            self.graph()

        interactive = ipywidgets.interactive(self.on_update, **widgets)
        if self.DEBUG:
            display(interactive)
