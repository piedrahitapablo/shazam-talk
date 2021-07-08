from talk.utils.math import TIME, superposed_waves
from talk.utils.slides import GraphWithWidgetsSlide
import ipywidgets as widgets
import matplotlib.pyplot as plt


DEFAULT_PARAMS = [(1, 1)]


class SuperpositionSlide(GraphWithWidgetsSlide):
    def widgets(self):
        waves_params = widgets.Textarea(
            value=f"{DEFAULT_PARAMS[0][0]}, {DEFAULT_PARAMS[0][1]}\n",
            placeholder="Enter some waves parameters",
            description="*",
            layout=widgets.Layout(width="160px", height="200px"),
        )

        box = widgets.HBox(children=[waves_params])
        ws = {"waves_params": waves_params}

        return box, ws

    def graph(self):
        self.fig, ax = plt.subplots()
        self.add_axes_lines(ax)

        (self.line,) = ax.plot(
            TIME, superposed_waves(TIME, DEFAULT_PARAMS), color="blue", lw=2
        )
        ax.set_xlabel("Time [s]")
        ax.set_ylabel("Amplitude [m]")
        ax.set_ylim([-6, 6])

    def on_update(self, waves_params):
        lines = waves_params.split("\n")
        waves = []
        for line in lines:
            a, f = line.split(",")
            waves.append((float(a), float(f)))

        self.line.set_ydata(superposed_waves(TIME, waves))
        self.fig.canvas.draw_idle()
