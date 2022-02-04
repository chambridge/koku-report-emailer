import os
import tempfile

import matplotlib.pyplot as plt
import pandas as pd


def plot_data(data):
    dates = []
    costs = []
    units = "USD"

    if not data:
        return (None, None)

    for datum in data:
        if (
            (datum.get("values") is not None)
            and (isinstance(datum.get("values"), list))
            and len(datum.get("values")) > 0
        ):
            values = datum["values"][0]
            units = values["cost"]["total"]["units"]
            dates.append(values["date"])
            costs.append(values["cost"]["total"]["value"])
        else:
            units = "USD"
            dates.append(datum["date"])
            costs.append(0.0)

    df = pd.DataFrame({"Dates": dates, units: costs}, index=dates)
    bar = df[units].plot.bar(title="Daily Cost", x="Dates", xlabel="Dates", y=units, ylabel=units)
    fig = bar.get_figure()
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    fig.savefig(tmp.name)
    return (tmp, tmp.name)
