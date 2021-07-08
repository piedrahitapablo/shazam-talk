from talk.utils.math import TIME, wave
from talk.utils.slides import GraphWithWidgetsSlide
import ipywidgets as widgets
import matplotlib.pyplot as plt


DEFAULT_AMPLITUDE = 5
DEFAULT_FREQUENCY = 0.5


class WavesSlide(GraphWithWidgetsSlide):
    def widgets(self):
        amplitude = widgets.FloatSlider(
            value=DEFAULT_AMPLITUDE,
            min=0,
            max=5,
            step=0.5,
            orientation="vertical",
            description=r"$A$",
        )
        frequency = widgets.FloatSlider(
            value=DEFAULT_FREQUENCY,
            min=0,
            max=5,
            step=0.5,
            orientation="vertical",
            description=r"$f$",
        )

        box = widgets.HBox(children=[amplitude, frequency])
        ws = {"amplitude": amplitude, "frequency": frequency}

        return box, ws

    def graph(self):
        self.fig, ax = plt.subplots()
        self.add_axes_lines(ax)

        (self.line,) = ax.plot(
            TIME, wave(TIME, DEFAULT_AMPLITUDE, DEFAULT_FREQUENCY), color="blue", lw=2
        )
        ax.set_xlabel("Time [s]")
        ax.set_ylabel("Amplitude [m]")
        ax.set_ylim([-6, 6])

    def on_update(self, amplitude, frequency):
        self.line.set_ydata(wave(TIME, amplitude, frequency))
        self.fig.canvas.draw_idle()
