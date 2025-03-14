"""Simple"""

from pyiem.network import Table as NetworkTable
from pyiem.plot import MapPlot


def main():
    """GO"""
    nt = NetworkTable("WFO")

    data = {}
    for sid in nt.sts:
        data[sid if len(sid) == 3 else sid[1:]] = 5

    data["DMX"] = 10
    data["DVN"] = 2

    mp = MapPlot(
        sector="conus",
        axisbg="white",
        title="Weather Bureau Office Coolness Factor",
    )
    mp.fill_cwas(
        data,
        bins=range(0, 11),
        lblformat="%.0f",
        units="awesome",
        ilabel=True,
        extend="neither",
    )
    mp.postprocess(filename="coolness.png")


if __name__ == "__main__":
    main()
