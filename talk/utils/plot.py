from functools import partial
from IPython.display import display
import ipywidgets
import matplotlib.pyplot as plt


def graph_w_axes(plots, x_label=None, y_label=None):
    fig, ax = plt.subplots()

    plt.grid(True, which="both")
    plt.axhline(y=0, color="k")
    plt.axvline(x=0, color="k")
    ax.set_facecolor("white")

    lines = []
    for plot in plots:
        (line,) = plt.plot(plot.pop("x"), plot.pop("y"), **plot)
        lines.append(line)

    if x_label is not None:
        ax.set_xlabel(x_label)
    if y_label is not None:
        ax.set_ylabel(y_label)

    return fig, ax, lines


def graph_w_widgets(graph, widgets=None, on_update=None, debug=False):
    if widgets is None:
        widgets = []

    v_boxes = []
    all_widgets = {}
    for ws in widgets:
        v_boxes.append(
            ipywidgets.VBox(
                children=tuple(ws.values()),
                layout=ipywidgets.Layout(display="flex", align_items="center"),
            )
        )
        all_widgets.update(ws)

    output = ipywidgets.Output()
    display(
        ipywidgets.HBox(
            children=[*v_boxes, output],
            layout=ipywidgets.Layout(display="flex", align_items="center"),
        ),
    )

    with output:
        lines_spec = graph.pop("lines")
        y_lims = graph.pop("y_lims", None)

        fig, ax, lines = graph_w_axes(lines_spec, **graph)
        if y_lims is not None:
            ax.set_ylim(y_lims)

    if on_update is not None:
        on_update_partial = partial(on_update, fig, lines)
        on_update_partial.__name__ = on_update.__name__
        w_interactive = ipywidgets.interactive(on_update_partial, **all_widgets)

        if debug:
            display(w_interactive)
