"""A plot of non-prego."""
import datetime

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import scipy.stats
import numpy as np

D9 = datetime.timedelta(days=280)
DATES = [
    [datetime.date(2010, 7, 24), datetime.date(2013, 1, 13) - D9],
    [datetime.date(2013, 1, 13), datetime.date(2014, 6, 15) - D9],
    [datetime.date(2014, 6, 15), datetime.date(2016, 12, 28) - D9],
    [datetime.date(2016, 12, 28), datetime.date(2018, 12, 16)],
]


def main():
    """Go Main Go."""
    x = []
    y = []
    for sts, ets in DATES:
        dates = pd.date_range(sts, ets)
        x.extend(list(dates.values))
        y.extend(list(range(0, len(dates))))
        if ets.year < 2018:
            x.append(ets + datetime.timedelta(days=1))
            y.append(0)

    (fig, ax) = plt.subplots(1, 1)
    ax.plot(x, y)
    ax.grid(True)
    ax.set_title("Consecutive Days Whereby Liz Was Not Pregnant")
    ax.set_ylabel("Consecutive Days")
    ax.set_xlabel("Date During Marriage Period")
    ax.set_ylim(bottom=-4)
    ax.axhline(y[-1], linestyle='-.', lw=2, color='r')

    plt.show()
    fig.savefig('plots/prego.eps')


if __name__ == '__main__':
    main()
