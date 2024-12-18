"""Plot car stuff."""

import pandas as pd
from pyiem.plot.use_agg import plt


def main():
    """Go Main Go."""
    vibe = pd.read_csv("vibe.csv")
    pilot = pd.read_csv("pilot.csv")
    df = pd.concat([vibe, pilot], ignore_index=True)
    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
    gdf = df.groupby(df["Date"].dt.year).sum(numeric_only=True)

    fig, ax = plt.subplots(1, 1)
    ax.set_position([0.12, 0.1, 0.75, 0.8])
    avgval = gdf["Trip"].mean() / 365.0
    ax.axhline(avgval, lw=2, color="k", zorder=3)
    bars = ax.bar(gdf.index.values, gdf["Trip"].to_numpy() / 365.0, zorder=4)
    bars[-1].set_color("r")
    for x, y in zip(gdf.index.values, gdf["Trip"].to_numpy() / 365.0):
        ax.text(
            x,
            y - 0.5,
            f"{y:.1f}",
            va="top",
            color="white",
            fontsize=12,
            rotation=90,
            ha="center",
            zorder=5,
        )
    ax.text(2024.75, avgval, f"Avg:\n{avgval:.1f}")
    ax.set_ylim(15, 47)
    ax.set_xlim(2007.4, 2024.6)
    """
    ax.annotate(
        "Wife has nicer car now\nso miles offloaded",
        xy=(2015, 900.0),
        xycoords="data",
        xytext=(-170, 90),
        textcoords="offset points",
        bbox=dict(boxstyle="round", fc="0.8"),
        arrowprops=dict(
            arrowstyle="->", connectionstyle="angle,angleA=0,angleB=90,rad=1"
        ),
    )
    ax.annotate(
        "Environment destroying\nSUV purchased",
        xy=(2018, 1750.0),
        xycoords="data",
        xytext=(-150, 3),
        textcoords="offset points",
        bbox=dict(boxstyle="round", fc="0.8"),
        arrowprops=dict(
            arrowstyle="->", connectionstyle="angle,angleA=0,angleB=90,rad=1"
        ),
    )
    """
    ax.set_xlabel("Year")
    ax.set_ylabel(r"Daily Driving Pain mi d$^{-1}$")
    ax.set_title(
        "'IEM1' Miles Driven per Day\n" "2008 Pontiac Vibe + 2018 Honda Pilot"
    )
    ax.grid(True)
    fig.savefig("f1_2024.eps")


if __name__ == "__main__":
    main()
