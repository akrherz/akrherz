"""A plot of heights."""
from io import StringIO

from metpy.units import units
import numpy as np
from pyiem.plot.use_agg import plt
import pandas as pd
from scipy.stats import linregress

data = """
age Charlotte Robert Maggie
1 28.25 29.25 30
1.5 31.25 32.25 33.25
2 33.5 35 35.25
2.5 35.5 36.5 36
3 37 38 37.5
3.5 38.75 39.75 39.5
4 40.5 42 41.25
4.5 41.75 42.25 43
5 42.75 44 44.25
5.5 44 45.5 46
6  47 47
6.5  48 48.75
7  49.75 50.25
7.5  51 51.25
8  52 52.25
8.5   52.75
9   53.75
9.5   54.75"""


def inch2mm(val):
    """Units"""
    return (val * units("inch")).to(units("cm")).m


def main():
    """Go Main Go."""
    df = pd.read_csv(StringIO(data), delimiter=" ", index_col="age")
    (fig, ax) = plt.subplots()
    ax.set_position([0.08, 0.1, 0.8, 0.8])
    colors = ["r", "g", "b"]
    markers = ["v", "o", "x"]
    for c, mk, name in zip(colors, markers, ["Charlotte", "Robert", "Maggie"]):
        df2 = df[~pd.isna(df[name])]
        xaxis = np.array([df2.index.values[-1] - 1, 18])
        ax.plot(df2.index, df2[name], color=c, marker=mk, label=name, markevery=4)
        hs, hint, _, _, _ = linregress(df2.index.values, df2[name].values)
        ys = xaxis * hs + hint
        ax.plot(xaxis, ys, color=c, linestyle="--", marker=mk)
        print(name, ys[-1])
        z = np.polyfit(df2.index.values, df2[name].values, 4)
        f = np.poly1d(z)
        xaxis = np.arange(df2.index.values[-1], 18.5, 0.5)
        # ax.plot(xaxis, f(xaxis), color=c, linestyle="-.", marker=mk, markevery=4)
    ax.grid(True)
    ax.legend(loc=2, ncol=3)
    ax.set_xlim(0, 19)
    ax.set_xticks(range(0, 19, 3))
    ax.set_ylim(28, 90)
    ax.set_title("Children's Observed and Linear Extrapolated Height")
    ax.set_xlabel(r"Age ($years$)")
    ax.set_ylabel(r"Height ($ft$)")
    ax.set_yticks(range(36, 85, 12))
    ax.set_yticklabels(range(3, 8))

    ax2 = ax.twinx()
    ax2.set_position([0.08, 0.1, 0.8, 0.8])
    ax2.set_ylim(inch2mm(28), inch2mm(90))
    ax2.set_yticks([inch2mm(x) for x in range(36, 85, 12)])
    ax2.set_ylabel(r"Height ($cm$)")

    # inset axes....
    axins = ax.inset_axes([0.05, 0.5, 0.35, 0.35])
    for c, mk, name in zip(colors, markers, ["Charlotte", "Robert", "Maggie"]):
        df2 = df[~pd.isna(df[name])]
        xaxis = np.array([df2.index.values[-1] - 1, 18])
        axins.plot(df2.index, df2[name], color=c, marker=mk, label=name)
    # sub region of the original image
    x1, x2, y1, y2 = 4, 6, 40, 48
    axins.set_xlim(x1, x2)
    axins.set_ylim(y1, y2)
    axins.set_xticklabels([])
    axins.set_yticklabels([])

    ax.indicate_inset_zoom(axins, edgecolor="black")

    fig.savefig("plots/2022_f1.eps")


if __name__ == "__main__":
    main()
