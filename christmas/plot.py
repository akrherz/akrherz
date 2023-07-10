import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import scipy.stats
import numpy as np

x = [
    datetime.date(2010, 7, 24),
    datetime.date(2013, 1, 13),
    datetime.date(2014, 6, 15),
    datetime.date(2017, 1, 17),
]
y = [2, 3, 4, 5]

d = [(x1 - x[0]).days for x1 in x]

h_slope, intercept, h_r_value, p_value, std_err = scipy.stats.linregress(d, y)

(fig, ax) = plt.subplots(1, 1)
ax.scatter(x, y, label="Actual", s=50, marker="s", color="r")
ax.set_ylabel("Number of Humans in Family")

x.append(datetime.date(2020, 1, 1))
d = np.array([(x1 - x[0]).days for x1 in x])
y = d * h_slope + intercept

ax.plot(x, y, label="Fit + Extrapolation", lw=3)

ax.set_title("Herzmann Family Size\nFamily Size on 1 Jan 2020: %.8f" % (y[-1],))
ax.legend(loc=4, ncol=2, fontsize=18)
ax.set_xticks(x)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%-d %b\n%Y"))
ax.grid(True)

fig.savefig("plots/size.eps")
