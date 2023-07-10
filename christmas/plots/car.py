"""Plot car stuff."""

from pyiem.plot.use_agg import plt
import pandas as pd


def main():
    """Go Main Go."""
    vibe = pd.read_csv("vibe.csv", sep="\t")
    pilot = pd.read_csv("pilot.csv", sep="\t")
    df = pd.concat([vibe, pilot], ignore_index=True)
    df["DATE"] = pd.to_datetime(df["DATE"], format="%m/%d/%Y")
    gdf = df.groupby(df["DATE"].dt.year).sum()

    fig, ax = plt.subplots(1, 1)
    ax.set_position([0.12, 0.1, 0.75, 0.8])
    avgval = gdf["TOTAL"].mean()
    ax.axhline(avgval, lw=2, color="k", zorder=3)
    bars = ax.bar(gdf.index.values, gdf["TOTAL"].values, zorder=4)
    bars[-1].set_color("r")
    for x, y in zip(gdf.index.values, gdf["TOTAL"].values):
        ax.text(
            x,
            y - 100,
            f"{y:.2f}",
            va="top",
            bbox=dict(color="white"),
            fontsize=8,
            rotation=90,
            ha="center",
            zorder=5,
        )
    ax.text(2020.75, avgval, f"Avg:\n${avgval:.2f}")
    ax.set_ylim(0, 2000)
    ax.set_xlim(2007.4, 2020.6)
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

    ax.set_xlabel("Year")
    ax.set_ylabel("Gasoline Outlay (US Dollars)")
    ax.set_title(
        "'IEM1' Yearly Gasoline Expenditure\n" "2008 Pontiac Vibe + 2018 Honda Pilot"
    )
    ax.grid(True)
    fig.savefig("f3_2020.eps")


if __name__ == "__main__":
    main()
