from talk.utils.math import (
    TIME,
    TIME_0,
    TIME_1,
    sampling_times,
    superposed_waves,
    wave,
    whittaker_shannon,
)
from talk.utils.slides import GraphWithWidgetsSlide
import ipywidgets as widgets
import matplotlib.pyplot as plt


class SamplingSlide(GraphWithWidgetsSlide):
    use_superposition = False

    def wave(self, time):
        if self.use_superposition:
            return superposed_waves(time, [(1, 1), (0.8, 1.7), (0.5, 2)])

        return wave(time, 1, 1)

    def widgets(self):
        use_superposition = widgets.Checkbox(
            value=False,
            description="Superposition",
            disabled=False,
            indent=False,
            layout=widgets.Layout(width="145px"),
        )
        show_reconstruction = widgets.Checkbox(
            value=False,
            description="Show reconstruction",
            disabled=False,
            indent=False,
            layout=widgets.Layout(width="145px"),
        )
        sampling_frequency = widgets.FloatSlider(
            min=0.1,
            max=15,
            step=0.1,
            orientation="vertical",
            description="Sampling frequency",
        )

        box = widgets.VBox(
            children=[use_superposition, show_reconstruction, sampling_frequency]
        )
        ws = {
            "use_superposition": use_superposition,
            "show_reconstruction": show_reconstruction,
            "sampling_frequency": sampling_frequency,
        }

        return box, ws

    def graph(self):
        self.fig, ax = plt.subplots()
        self.add_axes_lines(ax)

        s_times = sampling_times(TIME_0, TIME_1, 0.1)
        samples = self.wave(s_times)

        (self.signal_line,) = ax.plot(TIME, self.wave(TIME), color="gray", lw=2)
        (self.rec_line,) = ax.plot(
            TIME,
            whittaker_shannon(TIME, samples, s_times),
            color="red",
            linestyle="",
            lw=2,
        )
        (self.samples_line,) = ax.plot(
            s_times, samples, color="red", linestyle="", marker="o"
        )
        ax.set_xlabel("Time [s]")
        ax.set_ylabel("Amplitude [m]")
        ax.set_ylim([-2.5, 2.5])

    def on_update(
        self,
        use_superposition,
        show_reconstruction,
        sampling_frequency,
    ):
        self.use_superposition = use_superposition

        s_times = sampling_times(TIME_0, TIME_1, sampling_frequency)
        samples = self.wave(s_times)

        self.signal_line.set_ydata(self.wave(TIME))
        self.rec_line.set_ydata(whittaker_shannon(TIME, samples, s_times))
        self.samples_line.set_xdata(s_times)
        self.samples_line.set_ydata(samples)

        if show_reconstruction:
            self.rec_line.set_linestyle("-")
            self.samples_line.set_color("black")
        else:
            self.rec_line.set_linestyle("")
            self.samples_line.set_color("red")

        self.fig.canvas.draw_idle()
